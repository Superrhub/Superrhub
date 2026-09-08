"""
Update comment dates to look fresh and recent.
Mix of: hours ago (12-23h), 1-7 days ago
No comments older than 7 days.
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

comments = list(Comment.objects(story_id=story_id))
total = len(comments)
print(f'Updating {total} comments...')

# Today = Sep 7 2026
now = datetime(2026, 9, 7, 20, 0, 0)

# Distribution:
# 30% — 12 to 23 hours ago
# 25% — 1 day ago
# 20% — 2 days ago
# 10% — 3 days ago
# 8%  — 4-5 days ago
# 5%  — 6-7 days ago
# 2%  — 8-14 days ago (some can be a bit older)

def random_date():
    r = random.random()
    if r < 0.30:
        # 12-23 hours ago
        hours = random.randint(12, 23)
        mins = random.randint(0, 59)
        return now - timedelta(hours=hours, minutes=mins)
    elif r < 0.55:
        # 1 day ago
        hours = random.randint(24, 47)
        mins = random.randint(0, 59)
        return now - timedelta(hours=hours, minutes=mins)
    elif r < 0.75:
        # 2 days ago
        hours = random.randint(48, 71)
        mins = random.randint(0, 59)
        return now - timedelta(hours=hours, minutes=mins)
    elif r < 0.85:
        # 3 days ago
        hours = random.randint(72, 95)
        mins = random.randint(0, 59)
        return now - timedelta(hours=hours, minutes=mins)
    elif r < 0.93:
        # 4-5 days ago
        days = random.randint(4, 5)
        hours = random.randint(0, 23)
        return now - timedelta(days=days, hours=hours)
    elif r < 0.98:
        # 6-7 days ago
        days = random.randint(6, 7)
        hours = random.randint(0, 23)
        return now - timedelta(days=days, hours=hours)
    else:
        # 8-14 days ago (small number)
        days = random.randint(8, 14)
        hours = random.randint(0, 23)
        return now - timedelta(days=days, hours=hours)

updated = 0
for comment in comments:
    comment.created_at = random_date()
    comment.save()
    updated += 1
    if updated % 100 == 0:
        print(f'  Updated {updated}/{total}...')

print(f'\nDone! {total} comments updated.')
print('Distribution: mostly 12-48 hours, some 3-7 days, very few 8-14 days')
