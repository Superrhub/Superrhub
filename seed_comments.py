"""
Seeds 1000+ realistic comments on My Jannah story.
Run: python seed_comments.py
"""

import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.stories.models import Story
from apps.interactions.models import Comment

# Get the story
story = Story.objects(title__icontains='Jannah').first()
if not story:
    print('Story not found. Run seed_myjannah.py first.')
    exit()

story_id = str(story.id)

# Clear existing comments
Comment.objects(story_id=story_id).delete()
print('Cleared existing comments.')

# Usernames — diverse Nigerian/Muslim names
USERNAMES = [
    'FatimaLove', 'AbdullahReads', 'HauwaFan', 'NajibuWrites', 'ZainabHeart',
    'MubarakReader', 'AishaStories', 'UmarBooks', 'KhadijaLit', 'YusufReads',
    'MariyamWords', 'IbrahimPen', 'SumayyyaH', 'HamzaLoves', 'RuqayyaReads',
    'Sulaiman_', 'NafisaBooks', 'AbdulReads', 'ZaraNig', 'HakimWords',
    'FatihaLoves', 'MuhammadFan', 'AminaReads', 'UwaisStories', 'BasiraH',
    'TalhaNig', 'SafiyyaReads', 'HudaBooks', 'MasudWords', 'RaihanahFan',
    'KawtharLit', 'AbdulazizR', 'NusaybahH', 'BilaelReads', 'AsiyaStories',
    'DaudWords', 'SumayyaFan', 'HarunBooks', 'NafisaLit', 'ZubairReads',
    'JameelaH', 'SalmaNig', 'WalidWords', 'HannahReads', 'IsmailFan',
    'RoqayyaLit', 'SaadBooks', 'FaridaH', 'MansurReads', 'LatifaStories',
    'reader_ng01', 'bookworm_NG', 'StoriesNG', 'LoveReads_', 'FaithReader',
    'NigeriaBooks', 'HalalLove_', 'IslamicLit', 'NorthernNG', 'AbujaBks',
    'LagosReader', 'KanoBooks_', 'KadunaLit', 'ZariaReads', 'SokotoFan',
    'MaiduguriH', 'BauchiWords', 'GombeReader', 'AdamawaLit', 'TarabaFan',
    'NasarawaR', 'KebbiBks', 'ZamfaraLit', 'JigawaFan', 'KatsinaR',
    'IbadanRead', 'EnuguLit', 'AbujaFan_', 'PortHRead', 'CalabBooks',
    'AkoureReader', 'BenCityLit', 'WarriFan', 'AsabaReads', 'OnitBooks',
    'heart_reader', 'deep_feeler', 'emotional_', 'bookish_ng', 'quiet_reads',
    'night_reader', 'soul_words', 'love_pages', 'faith_reads', 'pure_heart',
    'gentle_soul', 'deep_roots', 'strong_faith', 'soft_words', 'warm_heart',
    'real_reader', 'true_love_', 'halal_read', 'modest_fan', 'sincere_r',
]

# Comment templates organized by emotion/theme
COMMENTS = [
    # Emotional/touching
    "This chapter made me cry. Subhanallah.",
    "I had to put my phone down after reading this. Too deep.",
    "Reading this at 2am and I can't stop crying.",
    "This hit different. Ya Allah.",
    "I feel everything in these words.",
    "Mubarak, you wrote my heart.",
    "This is not just a story. This is life.",
    "I have never related to a book this much.",
    "I read this twice and cried both times.",
    "This chapter is too real.",
    "The way you described that feeling... exactly.",
    "I felt every single word.",
    "This story is medicine for the heart.",
    "Reading this made me understand myself better.",
    "I needed this today. JazakAllahu Khairan.",

    # Praise for writing
    "The writing is so beautiful mashaAllah.",
    "You write like you have lived every word.",
    "This is some of the best writing I have read.",
    "MashaAllah your words flow like poetry.",
    "Every sentence carries weight.",
    "The way you express emotions is incredible.",
    "I wish I could write like this.",
    "This deserves to be published worldwide.",
    "The writing style is so unique and honest.",
    "You have a gift, Mubarak. Use it well.",

    # Faith-based reactions
    "May Allah reward you for this, Ameen.",
    "This reminded me to make dua for the one I love.",
    "SubhanAllah. Only Allah writes stories like this.",
    "This chapter on prayer is everything.",
    "The way faith runs through this story is beautiful.",
    "AlhamduliLlah for stories like this.",
    "May Allah give you your Jannah, in this world and the next.",
    "This story made me go back to Allah.",
    "The prayer chapter gave me chills. Allahu Akbar.",
    "May Allah bless the writer and the muse.",

    # Relating to personal experience
    "I went through something similar and this healed something in me.",
    "This is my story too.",
    "I thought I was the only one who felt this way.",
    "Thank you for putting into words what I couldn't.",
    "Every Muslim who has loved will understand this.",
    "I sent this to my sister. She cried too.",
    "Reading this reminded me of someone special.",
    "This is exactly what I experienced but could never explain.",
    "I shared this with my friends. We all related.",
    "You described the silence perfectly.",

    # Chapter-specific reactions
    "The breakfast chapter is so simple but so powerful.",
    "Chapter 21 — The Prayer — is my favourite chapter ever.",
    "Before Us hit me from the first paragraph.",
    "The Silence chapter is too accurate.",
    "The First Cracks... I felt that.",
    "My Jannah chapter made me smile and hurt at the same time.",
    "The Words We Could Not Take Back — every word is true.",
    "When I Wanted to Hold On made me realize something about myself.",
    "The Last Page Is Not Necessarily the End gave me hope.",
    "Just Friends chapter is the most painful thing I have read.",

    # Short emotional reactions
    "Wallahi this story is a blessing.",
    "I can't explain what I'm feeling right now.",
    "More please!",
    "Completed in one sitting. No regrets.",
    "This is what real love looks like.",
    "Honest. Raw. Beautiful.",
    "Every chapter is better than the last.",
    "I love this book so much.",
    "This is my comfort story.",
    "Please write more books Mubarak!",
    "Already recommending this to everyone I know.",
    "5 stars isn't enough.",
    "This story changed something in me.",
    "I will never forget this story.",
    "Completed. Heart full. Eyes wet.",

    # Supportive messages
    "Mubarak your courage to share this is admirable.",
    "Thank you for being honest about your mistakes.",
    "Real men admit when they are wrong. Respect.",
    "The accountability in this story is rare.",
    "You showed growth. That is what matters.",
    "This is what emotional maturity looks like.",
    "Thank you for showing that men feel too.",
    "Your vulnerability is your strength.",
    "Hauwa is lucky to have been loved like this.",
    "Whoever she is, she was truly cherished.",

    # Wishing well
    "May Allah unite you both if it is khair. Ameen.",
    "May your Jannah be real, in dunya and akhirah.",
    "Whatever happens, you both deserve peace.",
    "I pray Allah writes the best ending for you.",
    "May this story reach the heart it was written for.",
    "Ameen to every dua in this book.",
    "May Allah make it easy for you, Mubarak.",
    "May Hauwa read this someday and smile.",
    "May both of you find peace. Ameen.",
    "The best stories are the ones Allah writes.",

    # Nigerian flavor
    "See me seeing myself in this book chai.",
    "Mubarak abeg write more books like this.",
    "This man sha. The way he loves ehn.",
    "I don finish this book since yesterday.",
    "Northern Nigeria stories hit different walahi.",
    "This is better than any novel I have read.",
    "No be small thing this book do to me.",
    "I go recommend this to all my friends.",
    "This book entered my soul.",
    "Mubarak you are not ordinary.",
]

# Generate 1200 comments
print(f'Generating 1200 comments for: {story.title}')
print('This may take a moment...')

base_date = datetime(2024, 1, 20)
comments_to_insert = []

for i in range(1200):
    username = random.choice(USERNAMES)
    content = random.choice(COMMENTS)
    # Add some variation to avoid exact duplicates
    if random.random() < 0.3:
        extras = [
            ' ❤️', ' 😭', ' 🙏', ' MashaAllah!', ' Subhanallah!',
            ' Ameen!', ' 💯', ' So beautiful.', ' Wow.', ' Truly.'
        ]
        content += random.choice(extras)
    # Spread over time
    days_offset = random.randint(0, 200)
    hours_offset = random.randint(0, 23)
    comment_date = base_date + timedelta(days=days_offset, hours=hours_offset)

    comments_to_insert.append(Comment(
        user_id=f'reader_{i:04d}',
        username=username,
        story_id=story_id,
        content=content[:500],
        created_at=comment_date,
    ))

# Bulk insert in batches
batch_size = 100
for i in range(0, len(comments_to_insert), batch_size):
    batch = comments_to_insert[i:i + batch_size]
    for comment in batch:
        comment.save()
    print(f'  Inserted {min(i + batch_size, len(comments_to_insert))}/1200 comments...')

print()
print('=' * 50)
print(f'Done! 1200 comments added to "{story.title}"')
print('=' * 50)
