"""
Update chapter dates:
- All chapters written between January 2026 and April 13 2026
- Completed on Hauwa's birthday: 13 April 2026
"""
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.stories.models import Story

story = Story.objects(title__icontains='Jannah').first()

# 30 chapters from Jan 2026 to Apr 13 2026 (about 3.5 months)
chapter_dates = [
    datetime(2026, 1, 5),    # Ch 1
    datetime(2026, 1, 10),   # Ch 2
    datetime(2026, 1, 15),   # Ch 3
    datetime(2026, 1, 20),   # Ch 4
    datetime(2026, 1, 25),   # Ch 5
    datetime(2026, 1, 30),   # Ch 6
    datetime(2026, 2, 4),    # Ch 7
    datetime(2026, 2, 9),    # Ch 8
    datetime(2026, 2, 14),   # Ch 9
    datetime(2026, 2, 18),   # Ch 10
    datetime(2026, 2, 22),   # Ch 11
    datetime(2026, 2, 26),   # Ch 12
    datetime(2026, 3, 2),    # Ch 13
    datetime(2026, 3, 6),    # Ch 14
    datetime(2026, 3, 10),   # Ch 15
    datetime(2026, 3, 14),   # Ch 16
    datetime(2026, 3, 18),   # Ch 17
    datetime(2026, 3, 22),   # Ch 18
    datetime(2026, 3, 25),   # Ch 19
    datetime(2026, 3, 28),   # Ch 20
    datetime(2026, 3, 31),   # Ch 21
    datetime(2026, 4, 2),    # Ch 22
    datetime(2026, 4, 4),    # Ch 23
    datetime(2026, 4, 6),    # Ch 24
    datetime(2026, 4, 7),    # Ch 25
    datetime(2026, 4, 8),    # Ch 26
    datetime(2026, 4, 9),    # Ch 27
    datetime(2026, 4, 10),   # Ch 28
    datetime(2026, 4, 11),   # Ch 29
    datetime(2026, 4, 13),   # Ch 30 - Hauwa's birthday 🎂
]

for i, chapter in enumerate(story.chapters):
    if i < len(chapter_dates):
        chapter.created_at = chapter_dates[i]

story.created_at = datetime(2026, 1, 5)
story.updated_at = datetime(2026, 4, 13)
story.save()

print('Chapter dates updated:')
for ch in story.chapters:
    print(f'  Ch {ch.chapter_number:02d} — {ch.created_at.strftime("%d %b %Y")}  {ch.title[:40]}')

print()
print('Started:   05 January 2026')
print('Completed: 13 April 2026 — Hauwa birthday 🎂')
