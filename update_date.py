import os
from datetime import datetime
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
import django
django.setup()

from apps.stories.models import Story

s = Story.objects(title__icontains='Jannah').first()

# Hauwa's birthday — 13 April 2026
birthday = datetime(2026, 4, 13)

s.updated_at = birthday
s.created_at = datetime(2024, 1, 15)   # writing started
s.is_completed = True
s.save()

print('Story updated!')
print('Title:', s.title)
print('Completed on: 13 April 2026 (Hauwa birthday)')
print('Status: Completed =', s.is_completed)
