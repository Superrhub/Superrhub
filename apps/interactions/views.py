from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages

from .models import Like, Comment, ReadingList
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
