"""Add remaining comments to reach 1200+"""
import os, django, random
from datetime import datetime, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.stories.models import Story
from apps.interactions.models import Comment

story = Story.objects(title__icontains='Jannah').first()
story_id = str(story.id)
existing = Comment.objects(story_id=story_id).count()
print(f'Existing comments: {existing}')

needed = max(0, 1200 - existing)
print(f'Need to add: {needed} more')

USERNAMES = [
    'FatimaLove','AbdullahReads','HauwaFan','NajibuWrites','ZainabHeart',
    'MubarakReader','AishaStories','UmarBooks','KhadijaLit','YusufReads',
    'MariyamWords','IbrahimPen','SumayyyaH','HamzaLoves','RuqayyaReads',
    'heart_reader','deep_feeler','bookish_ng','quiet_reads','night_reader',
    'soul_words','love_pages','faith_reads','pure_heart','gentle_soul',
    'real_reader','true_love_','halal_read','modest_fan','sincere_r',
    'FaithReader','NigeriaBooks','HalalLove_','IslamicLit','NorthernNG',
    'KanoBooks_','ZariaReads','AbujaBks','LagosReader','BauchiWords',
]

COMMENTS = [
    "This chapter made me cry. Subhanallah.",
    "I had to put my phone down after reading this. Too deep.",
    "Reading this at 2am and I can't stop.",
    "This hit different. Ya Allah.",
    "Mubarak, you wrote my heart.",
    "This is not just a story. This is life.",
    "I have never related to a book this much.",
    "This chapter is too real.",
    "The way you described that feeling... exactly.",
    "This story is medicine for the heart.",
    "I needed this today. JazakAllahu Khairan.",
    "The writing is so beautiful mashaAllah.",
    "You write like you have lived every word.",
    "MashaAllah your words flow like poetry.",
    "Every sentence carries weight.",
    "This deserves to be published worldwide.",
    "May Allah reward you for this, Ameen.",
    "This reminded me to make dua for the one I love.",
    "SubhanAllah. Only Allah writes stories like this.",
    "The prayer chapter gave me chills. Allahu Akbar.",
    "I went through something similar and this healed me.",
    "This is my story too.",
    "Thank you for putting into words what I couldn't.",
    "Every Muslim who has loved will understand this.",
    "The breakfast chapter is so simple but so powerful.",
    "Chapter 21 is my favourite chapter ever.",
    "The Silence chapter is too accurate.",
    "The First Cracks... I felt that.",
    "My Jannah chapter made me smile and hurt at the same time.",
    "Wallahi this story is a blessing.",
    "I can't explain what I'm feeling right now.",
    "Completed in one sitting. No regrets.",
    "This is what real love looks like.",
    "Honest. Raw. Beautiful.",
    "I love this book so much.",
    "Please write more books Mubarak!",
    "5 stars isn't enough.",
    "This story changed something in me.",
    "Completed. Heart full. Eyes wet.",
    "May Allah unite you both if it is khair. Ameen.",
    "May your Jannah be real, in dunya and akhirah.",
    "May Allah write the best ending for you.",
    "Ameen to every dua in this book.",
    "See me seeing myself in this book chai.",
    "This man sha. The way he loves ehn.",
    "Northern Nigeria stories hit different walahi.",
    "This book entered my soul.",
    "Mubarak you are not ordinary.",
    "Real men admit when they are wrong. Respect.",
    "Your vulnerability is your strength.",
]

base_date = datetime(2024, 3, 1)
batch = []
for i in range(needed):
    username = random.choice(USERNAMES)
    content = random.choice(COMMENTS)
    if random.random() < 0.3:
        content += random.choice([' ❤️',' 😭',' 🙏',' MashaAllah!',' Ameen!'])
    days = random.randint(0, 180)
    hours = random.randint(0, 23)
    c = Comment(
        user_id=f'reader2_{i:04d}',
        username=username,
        story_id=story_id,
        content=content[:500],
        created_at=base_date + timedelta(days=days, hours=hours),
    )
    c.save()
    if (i+1) % 50 == 0:
        print(f'  Added {i+1}/{needed}...')

total = Comment.objects(story_id=story_id).count()
print(f'\nDone! Total comments: {total}')
