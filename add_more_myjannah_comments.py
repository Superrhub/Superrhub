import os, django, random
from datetime import datetime, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.stories.models import Story
from apps.interactions.models import Comment

story = Story.objects(title__icontains='My Jannah').first()
story_id = str(story.id)
existing = Comment.objects(story_id=story_id).count()
print(f'Existing: {existing}')

needed = max(0, 3000 - existing)
print(f'Adding {needed} more...')

USERNAMES = [
    'FatimaLove','AbdullahReads','HauwaFan','ZainabHeart','AishaStories',
    'UmarBooks','KhadijaLit','YusufReads','MariyamWords','IbrahimPen',
    'heart_reader','deep_feeler','bookish_ng','quiet_reads','night_reader',
    'soul_words','love_pages','faith_reads','pure_heart','gentle_soul',
    'real_reader','halal_read','FaithReader','NigeriaBooks','KanoBooks_',
    'LagosReader','BauchiWords','MubarakFan','AlibabaStar','NgReads',
    'SaharaWords','NileReads','reader_ng1','reader_ng2','bookworm01',
    'AdamawaLit','JigawaFan','KatsinaR','IbadanRead','AbujaFan',
    'AbujaBks','ZariaReads','NgLitFan','HausaReader','NaijaBooks',
    'IslamicLit','NorthernNG','AfricaLit','DeltaBooks','BenueReads',
]

COMMENTS = [
    "This chapter made me cry. Subhanallah.",
    "I had to put my phone down after reading this. Too deep.",
    "Mubarak, you wrote my heart.",
    "This is not just a story. This is life.",
    "I have never related to a book this much.",
    "The writing is so beautiful mashaAllah.",
    "MashaAllah your words flow like poetry.",
    "This deserves to be published worldwide.",
    "May Allah reward you for this, Ameen.",
    "SubhanAllah. Only Allah writes stories like this.",
    "The prayer chapter gave me chills. Allahu Akbar.",
    "I went through something similar and this healed me.",
    "Thank you for putting into words what I couldn't.",
    "The breakfast chapter is so simple but so powerful.",
    "Chapter 21 is my favourite chapter ever.",
    "Wallahi this story is a blessing.",
    "Completed in one sitting. No regrets.",
    "This is what real love looks like.",
    "5 stars isn't enough.",
    "This story changed something in me.",
    "May Allah unite you both if it is khair. Ameen.",
    "Ameen to every dua in this book.",
    "See me seeing myself in this book chai.",
    "Northern Nigeria stories hit different walahi.",
    "This book entered my soul.",
    "Mubarak you are not ordinary.",
    "I cried three times reading this book.",
    "The dedication alone made me emotional.",
    "Read this twice already. Different things hit each time.",
    "This book should be in every library in Nigeria.",
    "I shared this with my mom. She loved it.",
    "Every chapter is a lesson in love.",
    "The Last Page chapter brought me to tears.",
    "My Jannah is more than a book. It's a therapy.",
    "Reading this during Ramadan hit different.",
    "This is what halal love looks like written beautifully.",
    "Mubarak Ahmad Alibaba is a generational writer.",
    "30 chapters and every single one matters.",
    "I recommended this to my whole WhatsApp contact list.",
    "This book made me understand love better.",
    "The First Cracks chapter is too accurate walahi.",
    "Before Us is the best opening chapter I have ever read.",
    "The Silence chapter made me realize so much about myself.",
    "My Sugar Boy is great but My Jannah is the masterpiece.",
    "I laughed. I cried. I reflected. Perfect book.",
    "Allah bless this writer and protect his heart.",
    "I bought this for my sister as a gift. She couldn't stop crying.",
    "This is what I call Nigerian literature at its best.",
    "Every Muslim who has loved should read this book.",
    "The fact that this is a true story makes it hit 100x harder.",
]

# Spread over 30 days
now = datetime(2026, 9, 10, 20, 0, 0)
start = now - timedelta(days=30)
total_secs = int((now - start).total_seconds())

for i in range(needed):
    username = random.choice(USERNAMES)
    content = random.choice(COMMENTS)
    if random.random() < 0.25:
        content += random.choice([' ❤️',' 😭',' 🙏',' MashaAllah!',' Ameen!'])
    # Random time in the 30-day window
    secs = random.randint(0, total_secs)
    # Add some randomness to avoid bunching
    comment_time = start + timedelta(seconds=secs)
    Comment(
        user_id=f'jannah_extra_{i:05d}',
        username=username,
        story_id=story_id,
        content=content[:500],
        created_at=comment_time,
    ).save()
    if (i+1) % 200 == 0:
        print(f'  Added {i+1}/{needed}...')

total = Comment.objects(story_id=story_id).count()
print(f'Done! Total My Jannah comments: {total}')
