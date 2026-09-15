from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
import json, urllib.request, urllib.error

from .models import Like, Comment, ReadingList, Purchase
from apps.stories.models import Story
from apps.users.views import get_current_user


def toggle_like(request, story_id):
    current_user = get_current_user(request)
    if not current_user:
        return redirect('login')

    existing = Like.objects(
        user_id=str(current_user.id), story_id=story_id
    ).first()

    if existing:
        existing.delete()
        Story.objects(id=story_id).update_one(dec__likes_count=1)
        is_liked = False
    else:
        Like(user_id=str(current_user.id), story_id=story_id).save()
        Story.objects(id=story_id).update_one(inc__likes_count=1)
        is_liked = True

        # Send notification to story author
        story = Story.objects(id=story_id).first()
        if story and story.author_id != str(current_user.id):
            from .models import Notification
            Notification(
                recipient_id=story.author_id,
                sender_username=current_user.username,
                notif_type='like',
                story_id=story_id,
                story_title=story.title,
                message=f'{current_user.username} liked your story "{story.title}"',
            ).save()

    story = Story.objects(id=story_id).first()

    # HTMX partial response
    if request.headers.get('HX-Request'):
        html = render_to_string(
            'interactions/partials/like_button.html',
            {'story': story, 'is_liked': is_liked, 'story_id': story_id},
            request=request,
        )
        return HttpResponse(html)

    return redirect('story_detail', story_id=story_id)


def add_comment(request, story_id):
    current_user = get_current_user(request)
    if not current_user:
        return redirect('login')

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            Comment(
                user_id=str(current_user.id),
                username=current_user.username,
                story_id=story_id,
                content=content[:500],
            ).save()

            # Send notification to story author
            story = Story.objects(id=story_id).first()
            if story and story.author_id != str(current_user.id):
                from .models import Notification
                Notification(
                    recipient_id=story.author_id,
                    sender_username=current_user.username,
                    notif_type='comment',
                    story_id=story_id,
                    story_title=story.title,
                    message=f'{current_user.username} commented on "{story.title}": {content[:60]}...' if len(content) > 60 else f'{current_user.username} commented on "{story.title}": {content}',
                ).save()

    # HTMX partial response
    if request.headers.get('HX-Request'):
        comments = list(Comment.objects(story_id=story_id).order_by('created_at'))
        html = render_to_string(
            'interactions/partials/comments.html',
            {
                'comments': comments,
                'story_id': story_id,
                'current_user': current_user,
            },
            request=request,
        )
        return HttpResponse(html)

    return redirect('story_detail', story_id=story_id)


def delete_comment(request, comment_id):
    current_user = get_current_user(request)
    if not current_user:
        return redirect('login')

    comment = Comment.objects(id=comment_id).first()
    story_id = None
    if comment:
        story_id = comment.story_id
        if comment.user_id == str(current_user.id):
            comment.delete()

    if story_id:
        return redirect('story_detail', story_id=story_id)
    return redirect('home')


def toggle_reading_list(request, story_id):
    current_user = get_current_user(request)
    if not current_user:
        messages.error(request, 'Please log in to save stories.')
        return redirect('login')

    existing = ReadingList.objects(
        user_id=str(current_user.id), story_id=story_id
    ).first()

    if existing:
        existing.delete()
        messages.success(request, 'Removed from your reading list.')
    else:
        story = Story.objects(id=story_id).first()
        if story:
            ReadingList(
                user_id=str(current_user.id),
                story_id=story_id,
                story_title=story.title,
                author_username=story.author_username,
                cover_image=story.cover_image,
                genre=story.genre,
            ).save()
            messages.success(request, 'Added to your reading list.')

    return redirect('story_detail', story_id=story_id)


def reading_list_view(request):
    current_user = get_current_user(request)
    if not current_user:
        messages.error(request, 'Please log in to view your reading list.')
        return redirect('login')

    items = list(
        ReadingList.objects(user_id=str(current_user.id)).order_by('-added_at')
    )
    return render(request, 'interactions/reading_list.html', {
        'items': items,
        'current_user': current_user,
    })

def initiate_payment(request, story_id):
    """Initiate Paystack payment for premium story."""
    current_user = get_current_user(request)
    if not current_user:
        messages.error(request, 'Please log in to purchase.')
        return redirect('login')

    story = Story.objects(id=story_id).first()
    if not story:
        return redirect('home')

    # Already purchased
    existing = Purchase.objects(
        user_id=str(current_user.id), story_id=story_id, verified=True
    ).first()
    if existing:
        messages.info(request, 'You already have access to this story.')
        return redirect('story_detail', story_id=story_id)

    import os
    PAYSTACK_SECRET = os.getenv('PAYSTACK_SECRET_KEY', '')
    PAYSTACK_PUBLIC = os.getenv('PAYSTACK_PUBLIC_KEY', '')

    return render(request, 'interactions/payment.html', {
        'story': story,
        'current_user': current_user,
        'paystack_public_key': PAYSTACK_PUBLIC,
        'amount_kobo': story.price * 100,  # Paystack uses kobo
    })


def verify_payment(request, story_id):
    """Verify Paystack payment and grant access."""
    current_user = get_current_user(request)
    if not current_user:
        return redirect('login')

    reference = request.GET.get('reference', '')
    if not reference:
        messages.error(request, 'Payment reference missing.')
        return redirect('story_detail', story_id=story_id)

    import os
    PAYSTACK_SECRET = os.getenv('PAYSTACK_SECRET_KEY', '')

    # Verify with Paystack API
    try:
        url = f'https://api.paystack.co/transaction/verify/{reference}'
        req = urllib.request.Request(url)
        req.add_header('Authorization', f'Bearer {PAYSTACK_SECRET}')
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())

        if data.get('data', {}).get('status') == 'success':
            story = Story.objects(id=story_id).first()
            # Save purchase
            Purchase(
                user_id=str(current_user.id),
                story_id=story_id,
                amount=story.price if story else 0,
                reference=reference,
                verified=True,
            ).save()
            messages.success(request, f'Payment successful! You now have full access to "{story.title}".')
            return redirect('story_detail', story_id=story_id)
        else:
            messages.error(request, 'Payment could not be verified. Please contact support.')
            return redirect('story_detail', story_id=story_id)

    except Exception as e:
        messages.error(request, 'Payment verification failed. Please contact support.')
        return redirect('story_detail', story_id=story_id)


def has_access(user, story):
    """Check if user has access to a premium story."""
    if not story.is_premium:
        return True
    if not user:
        return False
    # Author always has access
    if story.author_id == str(user.id):
        return True
    # Check purchase
    return Purchase.objects(
        user_id=str(user.id), story_id=str(story.id), verified=True
    ).first() is not None


def notifications_view(request):
    current_user = get_current_user(request)
    if not current_user:
        return redirect('login')
    from .models import Notification
    notifications = list(
        Notification.objects(recipient_id=str(current_user.id)).order_by('-created_at')[:50]
    )
    # Mark all as read
    Notification.objects(
        recipient_id=str(current_user.id), is_read=False
    ).update(set__is_read=True)
    return render(request, 'interactions/notifications.html', {
        'notifications': notifications,
        'current_user': current_user,
    })


def unread_count(request):
    """Returns unread notification count as JSON."""
    current_user = get_current_user(request)
    if not current_user:
        return JsonResponse({'count': 0})
    from .models import Notification
    count = Notification.objects(
        recipient_id=str(current_user.id), is_read=False
    ).count()
    return JsonResponse({'count': count})


def continue_reading_view(request):
    current_user = get_current_user(request)
    if not current_user:
        return redirect('login')
    from .models import ReadingProgress
    progress_list = list(
        ReadingProgress.objects(user_id=str(current_user.id)).order_by('-updated_at')[:20]
    )
    return render(request, 'interactions/continue_reading.html', {
        'progress_list': progress_list,
        'current_user': current_user,
    })


def report_comment(request, comment_id):
    """POST — logged-in user reports a comment."""
    current_user = get_current_user(request)
    if not current_user:
        return JsonResponse({'error': 'Login required.'}, status=401)
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

    from .models import CommentReport
    reason = request.POST.get('reason', 'other').strip()
    valid_reasons = ['spam', 'hate', 'inappropriate', 'other']
    if reason not in valid_reasons:
        reason = 'other'

    # Prevent duplicate reports from the same user
    already = CommentReport.objects(
        comment_id=comment_id,
        reporter_id=str(current_user.id),
    ).first()
    if already:
        return JsonResponse({'status': 'already_reported'})

    comment = Comment.objects(id=comment_id).first()
    if not comment:
        return JsonResponse({'error': 'Comment not found.'}, status=404)

    CommentReport(
        comment_id=comment_id,
        comment_text=comment.content,
        reported_by=current_user.username,
        reporter_id=str(current_user.id),
        reason=reason,
    ).save()

    return JsonResponse({'status': 'reported'})


def pay_to_register(request):
    """Show Paystack checkout for ₦500 registration fee."""
    # Must have pending registration data
    pending = request.session.get('pending_registration')
    if not pending:
        return redirect('register')

    import os
    PAYSTACK_PUBLIC = os.getenv('PAYSTACK_PUBLIC_KEY', '')

    return render(request, 'auth/pay_to_register.html', {
        'pending': pending,
        'paystack_public_key': PAYSTACK_PUBLIC,
        'amount_kobo': 500 * 100,   # ₦500 in kobo
    })


def verify_registration_payment(request):
    """Verify ₦500 Paystack payment then create the account."""
    from .models import RegistrationPayment
    from apps.users.models import User

    reference = request.GET.get('reference', '')
    pending   = request.session.get('pending_registration')

    if not reference or not pending:
        messages.error(request, 'Registration session expired. Please try again.')
        return redirect('register')

    # Don't create duplicate accounts
    if User.objects(email=pending['email']).first():
        messages.error(request, 'This email is already registered. Please log in.')
        return redirect('login')

    import os, json, urllib.request, urllib.error
    PAYSTACK_SECRET = os.getenv('PAYSTACK_SECRET_KEY', '')

    try:
        url = f'https://api.paystack.co/transaction/verify/{reference}'
        req = urllib.request.Request(url)
        req.add_header('Authorization', f'Bearer {PAYSTACK_SECRET}')
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())

        if data.get('data', {}).get('status') == 'success':
            # Save payment record
            RegistrationPayment(
                reference=reference,
                email=pending['email'],
                verified=True,
            ).save()

            # Create the user account
            user = User(
                username=pending['username'],
                email=pending['email'],
                bio=pending.get('bio', ''),
                role=pending.get('role', 'reader'),
            )
            user.set_password(pending['password'])
            user.save()

            # Clear pending session data
            del request.session['pending_registration']

            # Log them in immediately
            request.session['user_id']  = str(user.id)
            request.session['username'] = user.username
            request.session['role']     = user.role

            messages.success(request, f'Welcome to SuperRHub, {user.username}! 🎉')
            return redirect('home')
        else:
            messages.error(request, 'Payment could not be verified. Please try again.')
            return redirect('pay_to_register')

    except Exception:
        messages.error(request, 'Payment verification failed. Please contact support.')
        return redirect('pay_to_register')
