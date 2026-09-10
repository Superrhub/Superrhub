import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from apps.stories.models import Story

covers = {
    'My Jannah': '/static/images/my jannah and mne .jpeg',
    'My Sugar Boy': '/static/images/my sugar boy .jpeg',
    'A Place Called Maybe': '/static/images/a place called.jpeg',
    'The Love We Choose': '/static/images/the love we choose .jpeg',
    'Conflict of Interest': '/static/images/conflict of interest.jpeg',
    'Tangled in Rivalry': '/static/images/tangled in revalry.jpeg',
}

for keyword, cover_url in covers.items():
    story = Story.objects(title__icontains=keyword[:12]).first()
    if story:
        story.cover_image = cover_url
        story.save()
        print(f'Updated: {story.title[:40]} → {cover_url}')
    else:
        print(f'Not found: {keyword}')

print('All covers updated!')
