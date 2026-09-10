import os, django, random
from datetime import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.stories.models import Story
from apps.interactions.models import Comment

s = Story.objects(title__icontains='My Jannah').first()
s.views_count = random.randint(352000, 385000)
s.likes_count = random.randint(18500, 22000)
s.save()
print(f'My Jannah: {s.views_count:,} views, {s.likes_count:,} likes')

# My Sugar Boy
sb = Story.objects(title__icontains='Sugar Boy').first()
if sb:
    sb.views_count = random.randint(45000, 68000)
    sb.likes_count = random.randint(3200, 5500)
    sb.save()
    print(f'My Sugar Boy: {sb.views_count:,} views, {sb.likes_count:,} likes')

# Other 4 books
for title in ['A Place Called Maybe', 'The Love We Choose', 'Conflict of Interest', 'Tangled in Rivalry']:
    story = Story.objects(title__icontains=title[:15]).first()
    if story:
        story.views_count = random.randint(12000, 35000)
        story.likes_count = random.randint(800, 4000)
        story.save()
        print(f'{story.title[:35]}: {story.views_count:,} views, {story.likes_count:,} likes')

print('Done!')
