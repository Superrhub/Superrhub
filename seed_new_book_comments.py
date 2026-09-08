"""
Add 150-200 comments to each of the 4 new books.
All comments dated today Sept 8, 2026 — from 6am to now (8pm).
"""
import os, django, random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.stories.models import Story
from apps.interactions.models import Comment

BOOK_TITLES = [
    'A Place Called Maybe',
    'The Love We Choose',
    'Conflict of Interest',
    'Tangled in Rivalry',
]

USERNAMES = [
    'FatimaLove', 'AbdullahReads', 'HauwaFan', 'ZainabHeart', 'AishaStories',
    'UmarBooks', 'KhadijaLit', 'YusufReads', 'MariyamWords', 'IbrahimPen',
    'SumayyyaH', 'HamzaLoves', 'RuqayyaReads', 'NafisaBooks', 'ZaraNig',
    'heart_reader', 'deep_feeler', 'bookish_ng', 'quiet_reads', 'night_reader',
    'soul_words', 'love_pages', 'faith_reads', 'pure_heart', 'gentle_soul',
    'real_reader', 'true_love_', 'halal_read', 'modest_fan', 'sincere_r',
    'FaithReader', 'NigeriaBooks', 'HalalLove_', 'IslamicLit', 'NorthernNG',
    'KanoBooks_', 'ZariaReads', 'AbujaBks', 'LagosReader', 'BauchiWords',
    'AdamawaLit', 'JigawaFan', 'KatsinaR', 'IbadanRead', 'EnuguLit',
    'reader_ng1', 'reader_ng2', 'reader_ng3', 'bookworm01', 'storyfan_',
    'MubarakFan', 'AlibabaStar', 'LoveSeries_', 'NgReads', 'AfricaLit',
    'SaharaWords', 'NileReads', 'DeltaBooks', 'NigerFan', 'BenueReads',
    'PlateauLit', 'KwaraFan', 'OgunReads', 'LagosLit', 'AbujaFan',
]

# Comments tailored for each book
COMMENTS_BY_BOOK = {
    'A Place Called Maybe': [
        "This title alone gives me chills. A Place Called Maybe. Wallahi.",
        "The uncertainty in this story is so real. I felt it.",
        "Chapter 1 already got me. I need more chapters NOW.",
        "Mubarak really knows how to start a story. SubhanAllah.",
        "The way he writes the beginning of feelings... exactly how it feels.",
        "I pre-ordered this in my heart already.",
        "Maybe is such a powerful word. This story understands that.",
        "The cover is so beautiful. The story matches it.",
        "I read the free chapters three times already.",
        "This is going to be my favourite book this year.",
        "The uncertainty, the hope... this is too real.",
        "I shared this with my sister. She cried reading chapter 1.",
        "MashaAllah the writing is so clean and honest.",
        "A Place Called Maybe hits different when you understand the title.",
        "The description alone made me want to read everything.",
    ],
    'The Love We Choose': [
        "Love is a choice. This book understands that deeply.",
        "Book 2 and it's already better than most full series I've read.",
        "The Love We Choose. I felt that title in my soul.",
        "Mubarak writes love the way it actually feels. Not perfect. Real.",
        "I finished the free chapters and I'm already unlocking the rest.",
        "This should be required reading for anyone who wants to love right.",
        "The way this story talks about choosing every day... I needed this.",
        "Chapter 2 made me think about my own choices. Beautiful.",
        "The Love Series just keeps getting better with every book.",
        "This author understands the heart walahi.",
        "I bought this immediately after reading the first chapter.",
        "Every Muslim who has loved needs to read this.",
        "The writing is so mature and honest. Respect Mubarak.",
        "I love how this book shows love as an action not just a feeling.",
        "Completed in one sitting. Worth every kobo.",
    ],
    'Conflict of Interest': [
        "Some connections aren't mistakes they're tests. WALLAHI THIS IS DEEP.",
        "Book 3 and he keeps raising the bar. MashaAllah.",
        "The conflict in this story is so real. I lived it.",
        "I have never related to a book title this much in my life.",
        "Conflict of Interest — I felt that from the first page.",
        "The way this story handles feelings and boundaries is incredible.",
        "Mubarak writes characters that feel like real people.",
        "I was crying by chapter 2. This is not a joke.",
        "The tests we face when we love someone... this book captures it.",
        "I unlocked the full book immediately. No regrets.",
        "This author is one of the best writers in Nigeria right now.",
        "Every chapter is a lesson. I'm highlighting everything.",
        "The Love Series Book 3 is the best one yet.",
        "Please never stop writing Mubarak. We need these stories.",
        "SubhanAllah this man's pen is blessed.",
    ],
    'Tangled in Rivalry': [
        "Two hearts. One journey. I am INVESTED.",
        "Book 4 and it just keeps getting better. How?!",
        "The rivalry to love pipeline is my favourite trope and this nails it.",
        "Tangled in Rivalry is such a perfect title. I felt it.",
        "I read all 3 free chapters without stopping. Now I'm buying.",
        "The slow burn in this story is everything I needed.",
        "Mubarak Ahmad Alibaba is seriously one of a kind.",
        "The way competition turns into connection here is so well written.",
        "I recommended this whole series to everyone in my contact list.",
        "Two rivals who fall for each other — a classic done perfectly.",
        "The Love Series is now my most recommended book series.",
        "I bought all 4 books today. Best decision I made this week.",
        "Chapter 3 of this book is my favourite chapter in the whole series.",
        "The chemistry between the characters in this book is incredible.",
        "Please release Book 5 soon Mubarak. We are WAITING.",
    ],
}

# Generic comments for all books
GENERIC_COMMENTS = [
    "Just discovered SuperHub because of Mubarak's books. Amazing platform.",
    "This author never disappoints. Every book is a masterpiece.",
    "I have read all 5 books now. My Jannah is still my favourite but this is close.",
    "The Love Series is exactly what Nigerian literature needed.",
    "Mubarak Ahmad Alibaba is a generational talent walahi.",
    "I cried, I laughed, I learned. This book did everything.",
    "Reading this during Fajr time. Can't put it down.",
    "The cover is beautiful. The story is even more beautiful.",
    "I found this on SuperHub and now I'm addicted to this author.",
    "5 stars isn't enough for this book.",
    "Already told my whole family about this series.",
    "This is the kind of story that changes you.",
    "Thank you Mubarak for writing stories that feel real.",
    "Nigerian romance fiction at its absolute finest.",
    "SubhanAllah. The way love is written in this series is something else.",
    "I read this in one sitting. My eyes hurt but I don't regret it.",
    "The series keeps getting better. Please don't stop writing.",
    "Bought this for my sister as a gift. She loved it too.",
    "This story understood something about me that I couldn't explain.",
    "MashaAllah the growth from book 1 to book 4 is incredible.",
]

# Today Sept 8 2026 — from 6am to 8pm
start_time = datetime(2026, 9, 8, 6, 0, 0)
end_time   = datetime(2026, 9, 8, 20, 0, 0)
total_minutes = int((end_time - start_time).total_seconds() / 60)

for title in BOOK_TITLES:
    story = Story.objects(title=title).first()
    if not story:
        print(f'Story not found: {title}')
        continue

    story_id = str(story.id)
    count = random.randint(150, 180)
    book_comments = COMMENTS_BY_BOOK.get(title, []) + GENERIC_COMMENTS

    print(f'Adding {count} comments to "{title}"...')

    for i in range(count):
        username = random.choice(USERNAMES)
        content = random.choice(book_comments)
        if random.random() < 0.25:
            content += random.choice([' ❤️', ' 😭', ' 🙏', ' MashaAllah!', ' Ameen!', ' 💯', ' Wow.'])

        # Random time today between 6am and 8pm
        minutes_offset = random.randint(0, total_minutes)
        comment_time = start_time + timedelta(minutes=minutes_offset)

        Comment(
            user_id=f'new_reader_{i:04d}_{title[:5]}',
            username=username,
            story_id=story_id,
            content=content[:500],
            created_at=comment_time,
        ).save()

    print(f'  Done! {count} comments added.')

print('\nAll comments seeded for today Sept 8, 2026!')

# Add views and likes to all 4 books
print('\nAdding views and likes...')
for title in BOOK_TITLES:
    story = Story.objects(title=title).first()
    if not story:
        continue
    story.views_count = random.randint(800, 2500)
    story.likes_count = random.randint(150, 600)
    story.save()
    print(f'  {title}: {story.views_count} views, {story.likes_count} likes')

print('\nDone! All 4 books have views, likes and comments.')

