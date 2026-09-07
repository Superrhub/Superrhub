import os, django, random
from datetime import datetime, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.interactions.models import Comment
from apps.stories.models import Story

story = Story.objects(title__icontains='Jannah').first()
story_id = str(story.id)

start = datetime(2026, 8, 23)
# Get comments NOT yet updated
old_comments = Comment.objects(story_id=story_id, created_at__lt=start)
count = old_comments.count()
print(f'Fixing {count} remaining comments...')

for i, comment in enumerate(old_comments):
    days = random.randint(0, 15)
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    comment.created_at = start + timedelta(days=days, hours=hours, minutes=minutes)
    comment.save()
    if (i+1) % 50 == 0:
        print(f'  Fixed {i+1}/{count}...')

print(f'Done! All comments now dated Aug 23 — Sep 7, 2026')
