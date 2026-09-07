import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
import django
django.setup()

from apps.stories.models import Story

s = Story.objects(title__icontains='Jannah').first()
s.cover_image = '/static/images/jannah.jpg'
s.save()

print('Cover updated:', s.cover_image)
