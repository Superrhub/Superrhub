from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import RegisterForm, LoginForm

# Admin username — only this user can access the admin panel
ADMIN_USERNAME = 'MubarakAhmedAlibaba'


def login_required_mongo(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            messages.error(request, 'Please log in to continue.')
            return redirect('login')
        return view_func(request, *args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')
        if request.session.get('username') != ADMIN_USERNAME:
            messages.error(request, 'Access denied.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


def get_current_user(request):
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
                role=data.get('role', 'reader'),
            )
            user.set_password(data['password'])
            user.save()
            request.session['user_id'] = str(user.id)
            request.session['username'] = user.username
            request.session['role'] = user.role
            messages.success(request, f'Welcome to SuperRHub, {user.username}! 🎉')
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
                request.session['role'] = user.role
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


# ===== ADMIN PANEL =====

@admin_required
def admin_dashboard(request):
    from apps.stories.models import Story
    from apps.interactions.models import Comment, Purchase

    total_users = User.objects.count()
    total_stories = Story.objects.count()
    total_comments = Comment.objects.count()
    total_purchases = Purchase.objects.count()
    total_revenue = sum(p.amount for p in Purchase.objects(verified=True))

    recent_users = list(User.objects.order_by('-created_at')[:10])
    recent_purchases = list(Purchase.objects(verified=True).order_by('-created_at')[:10])

    return render(request, 'admin/dashboard.html', {
        'current_user': get_current_user(request),
        'total_users': total_users,
        'total_stories': total_stories,
        'total_comments': total_comments,
        'total_purchases': total_purchases,
        'total_revenue': total_revenue,
        'recent_users': recent_users,
        'recent_purchases': recent_purchases,
    })


@admin_required
def admin_users(request):
    search = request.GET.get('search', '').strip()
    users = User.objects.order_by('-created_at')
    if search:
        from mongoengine.queryset.visitor import Q
        users = users.filter(Q(username__icontains=search) | Q(email__icontains=search))
    return render(request, 'admin/users.html', {
        'current_user': get_current_user(request),
        'users': list(users[:100]),
        'search': search,
    })


@admin_required
def admin_toggle_user(request, user_id):
    user = User.objects(id=user_id).first()
    if user and user.username != ADMIN_USERNAME:
        user.is_active = not user.is_active
        user.save()
        status = 'activated' if user.is_active else 'suspended'
        messages.success(request, f'{user.username} has been {status}.')
    return redirect('admin_users')


@admin_required
def admin_stories(request):
    from apps.stories.models import Story
    search = request.GET.get('search', '').strip()
    stories = Story.objects.order_by('-created_at')
    if search:
        stories = stories.filter(title__icontains=search)
    return render(request, 'admin/stories.html', {
        'current_user': get_current_user(request),
        'stories': list(stories[:100]),
        'search': search,
    })


@admin_required
def admin_toggle_story(request, story_id):
    from apps.stories.models import Story
    story = Story.objects(id=story_id).first()
    if story:
        story.is_published = not story.is_published
        story.save()
        status = 'published' if story.is_published else 'unpublished'
        messages.success(request, f'"{story.title}" has been {status}.')
    return redirect('admin_stories')


@admin_required
def admin_delete_story(request, story_id):
    from apps.stories.models import Story
    story = Story.objects(id=story_id).first()
    if story:
        title = story.title
        story.delete()
        messages.success(request, f'"{title}" deleted.')
    return redirect('admin_stories')


@admin_required
def admin_comments(request):
    from apps.interactions.models import Comment
    comments = list(Comment.objects.order_by('-created_at')[:200])
    return render(request, 'admin/comments.html', {
        'current_user': get_current_user(request),
        'comments': comments,
    })


@admin_required
def admin_delete_comment(request, comment_id):
    from apps.interactions.models import Comment
    comment = Comment.objects(id=comment_id).first()
    if comment:
        comment.delete()
        messages.success(request, 'Comment deleted.')
    return redirect('admin_comments')


@admin_required
def admin_purchases(request):
    from apps.interactions.models import Purchase
    from apps.stories.models import Story
    purchases = list(Purchase.objects(verified=True).order_by('-created_at')[:200])
    total_revenue = sum(p.amount for p in purchases)

    # Get story titles
    purchase_data = []
    for p in purchases:
        story = Story.objects(id=p.story_id).first()
        user = User.objects(id=p.user_id).first()
        purchase_data.append({
            'purchase': p,
            'story_title': story.title if story else 'Unknown',
            'username': user.username if user else 'Unknown',
        })

    return render(request, 'admin/purchases.html', {
        'current_user': get_current_user(request),
        'purchases': purchase_data,
        'total_revenue': total_revenue,
    })
