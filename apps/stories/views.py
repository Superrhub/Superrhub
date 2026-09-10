from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

from .models import Story, Chapter, GENRES
from .forms import StoryForm, ChapterForm
from apps.users.views import get_current_user, login_required_mongo


def home_view(request):
    current_user = get_current_user(request)
    latest = list(Story.objects(is_published=True).order_by('-created_at')[:6])
    popular = list(Story.objects(is_published=True).order_by('-views_count')[:6])
    return render(request, 'home.html', {
        'latest_stories': latest,
        'popular_stories': popular,
        'genres': GENRES,
        'current_user': current_user,
    })


def browse_view(request):
    current_user = get_current_user(request)
    genre = request.GET.get('genre', '').strip()
    search = request.GET.get('search', '').strip()
    page = max(1, int(request.GET.get('page', 1)))
    per_page = 20

    stories = Story.objects(is_published=True)
    if genre and genre in GENRES:
        stories = stories.filter(genre=genre)
    if search:
        # Search title, author, tags
        from mongoengine.queryset.visitor import Q
        stories = stories.filter(
            Q(title__icontains=search) |
            Q(author_username__icontains=search) |
            Q(tags__icontains=search)
        )
    stories = stories.order_by('-created_at')

    total = stories.count()
    start = (page - 1) * per_page
    stories_page = list(stories[start:start + per_page])
    has_next = total > page * per_page
    has_prev = page > 1

    return render(request, 'browse.html', {
        'stories': stories_page,
        'genres': GENRES,
        'current_genre': genre,
        'search': search,
        'page': page,
        'has_next': has_next,
        'has_prev': has_prev,
        'total': total,
        'current_user': current_user,
    })


def story_detail_view(request, story_id):
    current_user = get_current_user(request)
    try:
        story = Story.objects(id=story_id).first()
    except Exception:
        story = None

    if not story:
        messages.error(request, 'Story not found.')
        return redirect('home')

    Story.objects(id=story_id).update_one(inc__views_count=1)
    story.reload()

    from apps.interactions.models import Like, Comment, ReadingList, Purchase
    is_liked = False
    in_reading_list = False
    is_purchased = False
    if current_user:
        is_liked = Like.objects(
            user_id=str(current_user.id), story_id=story_id
        ).first() is not None
        in_reading_list = ReadingList.objects(
            user_id=str(current_user.id), story_id=story_id
        ).first() is not None
        is_purchased = Purchase.objects(
            user_id=str(current_user.id), story_id=story_id, verified=True
        ).first() is not None
        # Author always has access
        if story.author_id == str(current_user.id):
            is_purchased = True

    comments = list(Comment.objects(story_id=story_id).order_by('created_at'))
    is_author = current_user and story.author_id == str(current_user.id)

    return render(request, 'stories/detail.html', {
        'story': story,
        'current_user': current_user,
        'is_liked': is_liked,
        'in_reading_list': in_reading_list,
        'is_purchased': is_purchased,
        'comments': comments,
        'is_author': is_author,
    })


def reader_view(request, story_id, chapter_number):
    current_user = get_current_user(request)
    try:
        story = Story.objects(id=story_id).first()
    except Exception:
        story = None

    if not story:
        messages.error(request, 'Story not found.')
        return redirect('home')

    chapter = None
    for ch in story.chapters:
        if ch.chapter_number == chapter_number:
            chapter = ch
            break

    if not chapter:
        messages.error(request, 'Chapter not found.')
        return redirect('story_detail', story_id=story_id)

    # Premium paywall check
    if story.is_premium and chapter_number > story.free_chapters:
        from apps.interactions.views import has_access
        if not has_access(current_user, story):
            return redirect('initiate_payment', story_id=story_id)

    total_chapters = len(story.chapters)
    prev_num = chapter_number - 1 if chapter_number > 1 else None
    next_num = chapter_number + 1 if chapter_number < total_chapters else None

    # Save reading progress
    if current_user:
        from apps.interactions.models import ReadingProgress
        progress = ReadingProgress.objects(
            user_id=str(current_user.id), story_id=story_id
        ).first()
        if progress:
            progress.last_chapter = chapter_number
            progress.last_chapter_title = chapter.title
            progress.updated_at = datetime.utcnow()
            progress.save()
        else:
            ReadingProgress(
                user_id=str(current_user.id),
                story_id=story_id,
                story_title=story.title,
                cover_image=story.cover_image,
                author_username=story.author_username,
                last_chapter=chapter_number,
                last_chapter_title=chapter.title,
            ).save()

    return render(request, 'stories/reader.html', {
        'story': story,
        'chapter': chapter,
        'prev_num': prev_num,
        'next_num': next_num,
        'total_chapters': total_chapters,
        'current_user': current_user,
    })


@login_required_mongo
def create_story_view(request):
    current_user = get_current_user(request)
    form = StoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        tags = [t.strip() for t in data.get('tags', '').split(',') if t.strip()]
        story = Story(
            title=data['title'],
            description=data.get('description', ''),
            genre=data['genre'],
            tags=tags,
            cover_image=data.get('cover_image', ''),
            author_id=str(current_user.id),
            author_username=current_user.username,
            is_published=data.get('is_published', False),
            is_completed=data.get('is_completed', False),
        )
        story.save()
        messages.success(request, f'"{story.title}" created! Now add your first chapter.')
        return redirect('add_chapter', story_id=str(story.id))
    return render(request, 'stories/create.html', {
        'form': form,
        'current_user': current_user,
    })


@login_required_mongo
def edit_story_view(request, story_id):
    current_user = get_current_user(request)
    try:
        story = Story.objects(id=story_id).first()
    except Exception:
        story = None

    if not story or story.author_id != str(current_user.id):
        messages.error(request, 'You are not authorized to edit this story.')
        return redirect('home')

    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tags = [t.strip() for t in data.get('tags', '').split(',') if t.strip()]
            story.title = data['title']
            story.description = data.get('description', '')
            story.genre = data['genre']
            story.tags = tags
            story.cover_image = data.get('cover_image', '')
            story.is_published = data.get('is_published', False)
            story.is_completed = data.get('is_completed', False)
            story.updated_at = datetime.utcnow()
            story.save()
            messages.success(request, 'Story updated successfully.')
            return redirect('story_detail', story_id=story_id)
    else:
        initial = {
            'title': story.title,
            'description': story.description,
            'genre': story.genre,
            'tags': ', '.join(story.tags),
            'cover_image': story.cover_image,
            'is_published': story.is_published,
            'is_completed': story.is_completed,
        }
        form = StoryForm(initial=initial)

    return render(request, 'stories/edit.html', {
        'form': form,
        'story': story,
        'current_user': current_user,
    })


@login_required_mongo
def add_chapter_view(request, story_id):
    current_user = get_current_user(request)
    try:
        story = Story.objects(id=story_id).first()
    except Exception:
        story = None

    if not story or story.author_id != str(current_user.id):
        messages.error(request, 'You are not authorized to add chapters to this story.')
        return redirect('home')

    form = ChapterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        chapter_number = len(story.chapters) + 1
        chapter = Chapter(
            chapter_number=chapter_number,
            title=data['title'],
            content=data['content'],
        )
        story.chapters.append(chapter)
        story.updated_at = datetime.utcnow()
        story.save()
        messages.success(request, f'Chapter {chapter_number} — "{data["title"]}" added!')
        return redirect('add_chapter', story_id=story_id)

    return render(request, 'stories/add_chapter.html', {
        'form': form,
        'story': story,
        'current_user': current_user,
    })


@login_required_mongo
def my_stories_view(request):
    current_user = get_current_user(request)
    stories = list(
        Story.objects(author_id=str(current_user.id)).order_by('-created_at')
    )
    return render(request, 'stories/my_stories.html', {
        'stories': stories,
        'current_user': current_user,
    })


@login_required_mongo
def dashboard_view(request):
    current_user = get_current_user(request)
    from apps.interactions.models import Comment
    stories = list(Story.objects(author_id=str(current_user.id)).order_by('-views_count'))

    story_data = []
    total_views = 0
    total_likes = 0
    total_comments = 0
    max_views = 1
    max_likes = 1
    max_comments = 1

    for story in stories:
        comment_count = Comment.objects(story_id=str(story.id)).count()
        story_data.append({'story': story, 'comments': comment_count})
        total_views += story.views_count
        total_likes += story.likes_count
        total_comments += comment_count
        if story.views_count > max_views:
            max_views = story.views_count
        if story.likes_count > max_likes:
            max_likes = story.likes_count
        if comment_count > max_comments:
            max_comments = comment_count

    return render(request, 'stories/dashboard.html', {
        'stories': story_data,
        'total_stories': len(stories),
        'total_views': total_views,
        'total_likes': total_likes,
        'total_comments': total_comments,
        'max_views': max_views,
        'max_likes': max_likes,
        'max_comments': max_comments,
        'current_user': current_user,
    })


@login_required_mongo
def delete_story_view(request, story_id):
    current_user = get_current_user(request)
    try:
        story = Story.objects(id=story_id).first()
    except Exception:
        story = None

    if story and story.author_id == str(current_user.id):
        title = story.title
        story.delete()
        messages.success(request, f'"{title}" has been deleted.')
    else:
        messages.error(request, 'Story not found or not authorized.')
    return redirect('my_stories')


def leaderboard_view(request):
    current_user = get_current_user(request)
    from datetime import timedelta
    from apps.interactions.models import Comment

    # Top stories this week by views
    top_stories = list(Story.objects(is_published=True).order_by('-views_count')[:10])

    # Top stories by likes
    top_liked = list(Story.objects(is_published=True).order_by('-likes_count')[:10])

    # Top writers — aggregate by author
    from apps.users.models import User
    writer_stats = {}
    for story in Story.objects(is_published=True):
        uid = story.author_username
        if uid not in writer_stats:
            writer_stats[uid] = {'username': uid, 'views': 0, 'likes': 0, 'stories': 0}
        writer_stats[uid]['views'] += story.views_count
        writer_stats[uid]['likes'] += story.likes_count
        writer_stats[uid]['stories'] += 1

    top_writers = sorted(writer_stats.values(), key=lambda x: x['views'], reverse=True)[:10]

    return render(request, 'stories/leaderboard.html', {
        'top_stories': top_stories,
        'top_liked': top_liked,
        'top_writers': top_writers,
        'current_user': current_user,
    })
