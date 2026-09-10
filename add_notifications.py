import os, django, random
from datetime import datetime, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.interactions.models import Notification
from apps.users.models import User
from apps.stories.models import Story

author = User.objects(username='MubarakAhmedAlibaba').first()
if not author:
    print('Author not found')
    exit()

author_id = str(author.id)

# Clear old notifications
Notification.objects(recipient_id=author_id).delete()

stories = list(Story.objects(author_id=author_id, is_published=True))
now = datetime(2026, 9, 10, 20, 0, 0)

USERNAMES = [
    'FatimaLove','AbdullahReads','ZainabHeart','AishaStories','UmarBooks',
    'heart_reader','bookish_ng','MubarakFan','NgReads','LagosReader',
    'KanoBooks_','NigeriaBooks','soul_words','faith_reads','real_reader',
]

notif_types = ['like', 'comment', 'follow']
notif_messages = {
    'like': [
        '{username} liked your story "{title}"',
        '{username} loves "{title}" ❤️',
        '{username} gave your story a like',
    ],
    'comment': [
        '{username} commented on "{title}": "This is beautiful!"',
        '{username} commented on "{title}": "Wallahi this hit different 😭"',
        '{username} commented on "{title}": "MashaAllah the writing is amazing"',
        '{username} commented on "{title}": "This chapter made me cry"',
        '{username} commented on "{title}": "Best book I have read this year"',
    ],
    'follow': [
        '{username} started following you',
        '{username} is now following you',
    ],
}

notifications = []
for i in range(50):
    story = random.choice(stories)
    ntype = random.choice(notif_types)
    username = random.choice(USERNAMES)
    
    if ntype == 'follow':
        msg = random.choice(notif_messages['follow']).format(username=username)
        sid = ''
        stitle = ''
    else:
        msg = random.choice(notif_messages[ntype]).format(username=username, title=story.title[:30])
        sid = str(story.id)
        stitle = story.title
    
    days_ago = random.randint(0, 7)
    hours_ago = random.randint(0, 23)
    
    Notification(
        recipient_id=author_id,
        sender_username=username,
        notif_type=ntype,
        story_id=sid,
        story_title=stitle,
        message=msg,
        is_read=random.random() > 0.4,  # 40% unread
        created_at=now - timedelta(days=days_ago, hours=hours_ago),
    ).save()

print(f'Added 50 notifications for {author.username}')
unread = Notification.objects(recipient_id=author_id, is_read=False).count()
print(f'Unread: {unread}')
