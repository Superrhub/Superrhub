"""
Add views, likes and comments to My Sugar Boy.
All comments from today Sept 9, 2026 — 6am to now.
"""
import os, django, random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.stories.models import Story
from apps.interactions.models import Comment

story = Story.objects(title__icontains='Sugar Boy').first()
if not story:
    print('Story not found.')
    exit()

story_id = str(story.id)

# Add views and likes
story.views_count = random.randint(1200, 2800)
story.likes_count = random.randint(200, 500)
story.save()
print(f'Views: {story.views_count} | Likes: {story.likes_count}')

USERNAMES = [
    'FatimaLove', 'AbdullahReads', 'ZainabHeart', 'AishaStories',
    'UmarBooks', 'KhadijaLit', 'YusufReads', 'MariyamWords',
    'heart_reader', 'deep_feeler', 'bookish_ng', 'quiet_reads',
    'soul_words', 'love_pages', 'real_reader', 'true_love_',
    'FaithReader', 'NigeriaBooks', 'KanoBooks_', 'LagosReader',
    'reader_ng1', 'reader_ng2', 'bookworm01', 'storyfan_',
    'MubarakFan', 'AlibabaStar', 'NgReads', 'AfricaLit',
    'SaharaWords', 'NileReads', 'DeltaBooks', 'BenueReads',
    'NafisaBooks', 'ZaraNig', 'HamzaLoves', 'RuqayyaReads',
    'night_reader', 'gentle_soul', 'modest_fan', 'sincere_r',
]

COMMENTS = [
    "My Sugar Boy just broke my heart in the best way. Chapter 4 had me screaming.",
    "Jayden tearing that cheque... ICONIC. I rewound that scene three times.",
    "Vanessa is goals. Strong, wealthy, vulnerable. Real woman.",
    "The way Brian betrayed him!! I didn't see that coming at all.",
    "Chapter 13 confession scene made me cry on public transport. No shame.",
    "This book understands love better than most people do. Wallahi.",
    "Mubarak Ahmad Alibaba is NOT playing with us. Every chapter is a hit.",
    "Sugar Boy to CEO. The character development is INSANE.",
    "I finished this in one night. My eyes are hurting but I regret nothing.",
    "The age gap romance done RIGHT. No stereotypes. Just real feelings.",
    "Chapter 17 — The Price of Love — is my favourite chapter of all time.",
    "I bought the full access immediately after chapter 3. Worth every naira.",
    "My Sugar Boy taught me that independence is the greatest love language.",
    "The photograph drama had me so stressed. I was texting my friend updates.",
    "Vanessa's backstory in chapter 13 changed everything. Her fear made sense.",
    "This author writes Nigerian romance like nobody else.",
    "The ending made me smile so wide. They deserved each other.",
    "Already recommending this to everyone. Finished it at 3am.",
    "Chapter 9 where Brian asks 'what would you have?' hit different.",
    "The rules of the relationship chapter is everything. No lies. No control.",
    "I cried at The Empty Apartment chapter. Just vibes and silence.",
    "Selena coming back added just the right amount of drama.",
    "The way Vanessa tested him with that cheque... clever woman.",
    "This book should be a movie. I'm casting in my head already.",
    "Mubarak writes male vulnerability so honestly. Rare.",
    "Years Later chapter gave me chills. From Sugar Boy to award winner.",
    "The dedication at the start got me already: 'choose between what the world thinks is right and what the heart believes is real.'",
    "I feel seen by this book in ways I can't explain.",
    "My Sugar Boy and My Jannah together are a whole education in love.",
    "The last line: 'Only yours.' I felt that in my chest.",
    "Chapter 6 — Something Real — is when I knew this was different.",
    "Nigerian fiction is eating and this author is leading the charge.",
    "Just discovered SuperHub because someone shared this book. Grateful.",
    "The whispers and gossip chapters are so real. Society doesn't change.",
    "Jayden's mother's advice: 'Never let money speak louder than character.' Words to live by.",
    "I've read it twice already. Different details hit each time.",
    "Please make this a series. I need to know what happened with Brian.",
    "5 books by this author on SuperHub and every single one is a banger.",
    "I shared chapter 17 screenshot with my boyfriend. He understood the assignment.",
    "My Sugar Boy is proof that good storytelling doesn't need a million words. Just the right ones.",
    "Wallahi this man's pen is something else. SubhanAllah.",
    "The black Mercedes opening scene is so cinematic. I pictured it perfectly.",
    "From N3,450 in his account to company award winner. What a journey.",
    "I laughed, cried, got angry, forgave — all in one book. That's literature.",
    "The nickname Sugar Boy becoming a badge of honour at the end. Beautiful arc.",
    "Vanessa leaning closer and saying 'My sugar boy' at the end. TEARS.",
    "This book should be on every Nigerian university reading list.",
    "I'm buying physical copies when they're available. This deserves a shelf.",
    "The way this book handles money in relationships is so honest and mature.",
    "Already on my second read. Picking up things I missed the first time.",
]

# Today Sept 9 2026 — 6am to 9pm
start = datetime(2026, 9, 9, 6, 0, 0)
end   = datetime(2026, 9, 9, 21, 0, 0)
total_mins = int((end - start).total_seconds() / 60)

count = random.randint(160, 200)
print(f'Adding {count} comments...')

for i in range(count):
    username = random.choice(USERNAMES)
    content = random.choice(COMMENTS)
    if random.random() < 0.3:
        content += random.choice([' ❤️', ' 😭', ' 🙏', ' 🔥', ' Wow!', ' MashaAllah!'])
    mins = random.randint(0, total_mins)
    Comment(
        user_id=f'sb_reader_{i:04d}',
        username=username,
        story_id=story_id,
        content=content[:500],
        created_at=start + timedelta(minutes=mins),
    ).save()

print(f'Done! {count} comments added.')
print(f'Story: {story.title}')
print(f'Views: {story.views_count} | Likes: {story.likes_count} | Comments: {count}')
