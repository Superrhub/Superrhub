import os, django, random
from datetime import datetime, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.interactions.models import Comment
from apps.stories.models import Story
from mongoengine.connection import get_db
from bson import ObjectId

db = get_db()
comments_col = db['comments']

# Fix dates for ALL stories
stories = Story.objects(is_published=True)
now = datetime(2026, 9, 10, 20, 0, 0)

for story in stories:
    story_id = str(story.id)
    comments = list(Comment.objects(story_id=story_id).order_by('created_at'))
    if not comments:
        continue
    
    print(f'Fixing {len(comments)} comments for: {story.title[:40]}')
    
    # Spread comments over 15 days before now
    start = now - timedelta(days=15)
    current_time = start
    
    bulk_ops = []
    for i, comment in enumerate(comments):
        # Random gap between comments: 3 min to 4 hours
        gap_minutes = random.randint(3, 240)
        # Sometimes a burst (short gaps)
        if random.random() < 0.3:
            gap_minutes = random.randint(1, 15)
        # Sometimes a long gap (hours)
        if random.random() < 0.1:
            gap_minutes = random.randint(120, 480)
            
        current_time = current_time + timedelta(minutes=gap_minutes)
        
        # Don't go past now
        if current_time > now:
            current_time = now - timedelta(minutes=random.randint(5, 60))
        
        bulk_ops.append({
            'filter': {'_id': comment.id},
            'update': {'$set': {'created_at': current_time}},
        })
    
    # Execute in bulk batches of 500
    batch_size = 500
    for b in range(0, len(bulk_ops), batch_size):
        batch = bulk_ops[b:b+batch_size]
        from pymongo import UpdateOne
        comments_col.bulk_write([UpdateOne(op['filter'], op['update']) for op in batch])
    
    # Reload first and last for display
    first = comments[0]
    last = comments[-1]
    first.reload()
    last.reload()
    print(f'  Fixed. Range: {first.created_at.strftime("%b %d")} to {last.created_at.strftime("%b %d, %H:%M")}')

print('All comment dates fixed!')
