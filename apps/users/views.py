from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import RegisterForm, LoginForm


def login_required_mongo(view_func):
    """Decorator to require login for views."""
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            messages.error(request, 'Please log in to continue.')
            return redirect('login')
        return view_func(request, *args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


def get_current_user(request):
    """Get the currently logged-in user from session."""
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    try:
        return User.objects(id=user_id).first()
    except Exception:
        return None


def register_view(request):
    if request.session.get('user_id'):
        return redirect('home')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        if User.objects(username=data['username']).first():
            form.add_error('username', 'This username is already taken.')
        elif User.objects(email=data['email']).first():
            form.add_error('email', 'This email is already registered.')
        else:
            user = User(
                username=data['username'],
                email=data['email'],
                bio=data.get('bio', ''),
            )
            user.set_password(data['password'])
            user.save()
            request.session['user_id'] = str(user.id)
            request.session['username'] = user.username
            messages.success(request, f'Welcome to SuperHub, {user.username}! 🎉')
            return redirect('home')
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.session.get('user_id'):
        return redirect('home')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        user = User.objects(email=data['email']).first()
        if user and user.check_password(data['password']):
            if not user.is_active:
                form.add_error(None, 'Your account has been deactivated.')
            else:
                request.session['user_id'] = str(user.id)
                request.session['username'] = user.username
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home')
        else:
            form.add_error(None, 'Invalid email or password.')
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def profile_view(request, username):
    profile_user = User.objects(username=username).first()
    if not profile_user:
        messages.error(request, 'User not found.')
        return redirect('home')
    current_user = get_current_user(request)
    from apps.stories.models import Story
    user_stories = Story.objects(
        author_id=str(profile_user.id), is_published=True
    ).order_by('-created_at')
    is_own = current_user and str(current_user.id) == str(profile_user.id)
    is_following = (
        current_user and str(profile_user.id) in current_user.following
    )
    return render(request, 'users/profile.html', {
        'profile_user': profile_user,
        'user_stories': user_stories,
        'is_own': is_own,
        'is_following': is_following,
        'current_user': current_user,
    })


@login_required_mongo
def edit_profile_view(request, username):
    current_user = get_current_user(request)
    if current_user.username != username:
        return redirect('profile', username=current_user.username)
    if request.method == 'POST':
        bio = request.POST.get('bio', '').strip()
        avatar = request.POST.get('avatar', '').strip()
        current_user.bio = bio[:500]
        if avatar:
            current_user.avatar = avatar
        current_user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile', username=current_user.username)
    return render(request, 'users/edit_profile.html', {'current_user': current_user})


def follow_view(request, username):
    current_user = get_current_user(request)
    if not current_user:
        messages.error(request, 'Please log in to follow users.')
        return redirect('login')
    target = User.objects(username=username).first()
    if not target or str(target.id) == str(current_user.id):
        return redirect('profile', username=username)
    target_id = str(target.id)
    requester_id = str(current_user.id)
    if target_id in current_user.following:
        current_user.following.remove(target_id)
        if requester_id in target.followers:
            target.followers.remove(requester_id)
        messages.success(request, f'You unfollowed {username}.')
    else:
        current_user.following.append(target_id)
        if requester_id not in target.followers:
            target.followers.append(requester_id)
        messages.success(request, f'You are now following {username}.')
    current_user.save()
    target.save()
    return redirect('profile', username=username)
