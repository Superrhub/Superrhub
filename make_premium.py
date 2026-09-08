import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
import django
django.setup()

from apps.stories.models import Story

s = Story.objects(title__icontains='Jannah').first()
s.is_premium = True
s.price = 500
s.free_chapters = 3
s.save()

print('My Jannah is now PREMIUM')
print('Price: N500')
print('Free chapters: 3')
print('Chapters 4-30 locked until payment')
