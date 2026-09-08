import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
import django
django.setup()

from apps.stories.models import Story

s = Story.objects(title__icontains='Jannah').first()
s.is_premium = True
s.price = 1000
s.free_chapters = 3
s.save()

print('Updated!')
print(f'Title: {s.title}')
print(f'Price: N{s.price}')
print(f'Free chapters: {s.free_chapters}')
print('Chapters 4-30 require N1000 payment')
