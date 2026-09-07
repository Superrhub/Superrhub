"""
Update all comment dates to be between April 13 2026 (publish date)
and September 7 2026 (today)
"""
import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.interactions.models import Comment
from apps.stories.models import Story

story = Story.objects(title__icontains='Jannah').first()
story_id = str(story.id)

comments = Comment.objects(story_id=story_id)
total = comments.count()
print(f'Updating {total} comments...')

# Date range: August 23 2026 to September 7 2026
start_date = datetime(2026, 8, 23)
end_date = datetime(2026, 9, 7)
date_range = (end_date - start_date).days  # 15 days

updated = 0
for comment in comments:
    days = random.randint(0, date_range)
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    comment.created_at = start_date + timedelta(days=days, hours=hours, minutes=minutes)
    comment.save()
    updated += 1
    if updated % 100 == 0:
        print(f'  Updated {updated}/{total}...')

print(f'\nDone! All {total} comments now dated Apr 13 — Sep 7, 2026')
