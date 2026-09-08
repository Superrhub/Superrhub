"""
Seeds 4 new books by Mubarak Ahmad Alibaba on SuperHub.
Run: python seed_4books.py
"""
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.users.models import User
from apps.stories.models import Story, Chapter

# Get the author
author = User.objects(username='MubarakAhmedAlibaba').first()
if not author:
    print('Author not found. Run seed_myjannah.py first.')
    exit()

print(f'Author: {author.username}')

BOOKS = [
    {
        'title': 'A Place Called Maybe',
        'cover': '/static/images/place-called-maybe.jpg',
        'description': (
            'Sometimes the heart finds what the mind doesn\'t expect. '
            'A story about two people who meet at the crossroads of certainty and doubt, '
            'and discover that love doesn\'t always arrive with a clear answer. '
            'Part of the My Jannah and Me series by Mubarak Ahmad Alibaba.'
        ),
        'genre': 'Romance',
        'tags': ['love', 'faith', 'Nigeria', 'halal', 'romance'],
        'price': 2500,
        'series': 'My Jannah and Me',
        'tagline': 'Sometimes the heart finds what the mind doesn\'t expect...',
        'chapters': [
            ('The Beginning of Maybe', 'Some stories don\'t start with a clear yes or no. They start with a maybe — a feeling that sits quietly in the chest, asking to be understood before it is acted upon.\n\nI never planned to feel the way I felt. Life rarely gives us a schedule for the moments that change us. But there are days when something ordinary becomes the door to something extraordinary, and you don\'t realize it until you are already walking through.\n\nThis is a story about that kind of beginning.'),
            ('The First Encounter', 'There are people you meet and immediately sense that something is different. Not because they say anything unusual, not because they do anything remarkable, but because their presence carries a weight that you cannot explain.\n\nShe was one of those people.\n\nI remember the first time I saw her clearly. Not just looked — but actually saw. And in that moment, something in me shifted. I didn\'t understand it then. I only understood it later, when understanding came with the ache of knowing too much too late.'),
            ('Questions Without Answers', 'The problem with falling for someone is that feelings don\'t wait for the right time. They arrive when they want to, often uninvited, often inconvenient, always honest.\n\nI began asking myself questions I had no answers to. Did she feel it too? Was I reading too much into ordinary kindness? Was this what they called connection, or was it simply familiarity mistaken for something deeper?\n\nMaybe. The word kept returning to me. Maybe this was real. Maybe it wasn\'t. Maybe the heart was wiser than the mind. Maybe it was just afraid.'),
            ('The Weight of Silence', 'Silence between two people can mean many things. It can mean there is nothing to say. It can mean there is too much. It can mean that words feel too small for what is being felt.\n\nBetween us, silence had grown into its own language. I learned to read her quiet. She, I think, learned to read mine. And in that unspoken space, something was building — slowly, carefully, the way things build when they are meant to last.'),
            ('A Place Called Maybe', 'I began to understand that not everything deserves a definite answer. Some things are meant to live in the space between yes and no. Some connections exist in the place called maybe — where hope is still alive, where possibility has not yet been closed.\n\nAnd sometimes, living in that place is not weakness. Sometimes it is the most honest thing you can do — to admit that you don\'t fully know, but you are willing to stay long enough to find out.\n\nThis is where our story began. In the place called maybe.'),
        ],
    },
    {
        'title': 'The Love We Choose',
        'cover': '/static/images/love-we-choose.jpg',
        'description': (
            'Sometimes the heart finds what the mind doesn\'t expect. '
            'Love is not only something that happens to us — it is something we decide, again and again, '
            'even when it is difficult. The Love We Choose is Book 2 of The Love Series by Mubarak Ahmad Alibaba.'
        ),
        'genre': 'Romance',
        'tags': ['love', 'choice', 'faith', 'Nigeria', 'halal', 'series'],
        'price': 2500,
        'series': 'The Love Series Book 2',
        'tagline': 'Sometimes the heart finds what the mind doesn\'t expect...',
        'chapters': [
            ('The Choice', 'Love, I have come to understand, is not only a feeling. It is a decision. It is something you choose — not once, but every day, through every difficulty, every silence, every moment when walking away would be easier.\n\nI learned this the hard way. I learned it in the middle of my own story, when the feeling alone was no longer enough and I had to decide: was I willing to do what love actually required?\n\nThis is the story of that choice.'),
            ('What Love Requires', 'Feelings are the beginning of love, not the whole of it. Feelings say: I notice you. I want to be near you. You make ordinary things feel worth living.\n\nBut love says: I will still be here when it is hard. I will still choose you when choosing you costs something. I will learn how to love you better, even when learning is uncomfortable.\n\nI was still at the beginning of that lesson when our story started. But I was willing to learn.'),
            ('The Weight of Wanting', 'There is a particular kind of pain that comes from wanting something you are not sure you should want. It is not the pain of loss — it is the pain of uncertainty. The pain of standing at a door and not knowing whether you should knock.\n\nI knew what I wanted. I was less certain about whether what I wanted was right, whether I was ready, whether the timing would be kind.\n\nBut I was learning that the heart does not always wait for certainty before it commits.'),
            ('Choosing Every Day', 'The love that lasts is not the love that arrives without effort. It is the love that is chosen — again and again, on ordinary days and difficult ones, in moments of warmth and moments of doubt.\n\nI chose. Not perfectly, not without fear, but with sincerity. And I believe that sincerity, even imperfect, is the foundation of something real.\n\nThis is what I understand about love now: it is not a destination. It is a daily act of choosing.'),
            ('The Love We Keep', 'Some loves are kept quietly. Not because they are small, but because they are precious. Because some things are sacred enough to protect from noise.\n\nThe love we choose is also the love we keep — through patience, through prayer, through the willingness to become better for the sake of someone who deserves our best.\n\nAnd that is the love I was learning to give.'),
        ],
    },
    {
        'title': 'Conflict of Interest',
        'cover': '/static/images/conflict-of-interest.jpg',
        'description': (
            'Some connections aren\'t mistakes — they\'re tests. '
            'When two people from different worlds find themselves drawn together, '
            'every feeling becomes a conflict, and every choice carries consequences. '
            'Book 3 of The Love Series by Mubarak Ahmad Alibaba.'
        ),
        'genre': 'Romance',
        'tags': ['love', 'conflict', 'faith', 'Nigeria', 'halal', 'series'],
        'price': 2500,
        'series': 'The Love Series Book 3',
        'tagline': 'Some connections aren\'t mistakes... they\'re tests.',
        'chapters': [
            ('The Conflict Begins', 'Not all conflicts are between enemies. Some of the hardest battles are fought between people who care about each other — between what they feel and what they know is right, between what they want and what faith requires.\n\nThis was that kind of conflict.\n\nTwo people. Two lives that were not supposed to intersect. And yet here we were, standing at the crossing, neither willing to step back, neither certain how to move forward.'),
            ('The Interest', 'Interest is a quiet thing at first. It doesn\'t announce itself loudly. It begins as simple attention — noticing someone a little more than others, finding yourself thinking about a conversation long after it has ended.\n\nBy the time you realize the interest has become something deeper, it has already taken root. And then the conflict truly begins: what do you do with something that feels right but lives in complicated territory?'),
            ('The Test', 'Some connections are tests. Not punishments — tests. Opportunities to see what you are made of, whether your character holds when feelings are strong and boundaries are unclear.\n\nI was being tested. I knew it. And knowing it made the test both harder and more meaningful. Because a test only has value if you face it honestly.'),
            ('Navigating the Conflict', 'The goal was never to eliminate the feeling. Feelings are not the problem — they are information. The question is what you do with them. Whether you let them control you or whether you use them to understand yourself better.\n\nI was learning to navigate. To feel without being ruled by feeling. To be honest about what I wanted while remaining faithful to what I believed was right.'),
            ('Resolution', 'Not every conflict ends with a clean resolution. Some conflicts teach you something and then quietly step back, leaving you changed but not destroyed.\n\nThis conflict left me with a clearer understanding of myself — my weaknesses, my values, and the kind of person I wanted to become. And sometimes, that is what a test is for. Not to defeat you. To define you.'),
        ],
    },
    {
        'title': 'Tangled in Rivalry',
        'cover': '/static/images/tangled-in-rivalry.jpg',
        'description': (
            'Two hearts. One journey. Love, choices, and everything in between. '
            'When rivalry becomes the unlikely path to connection, '
            'two people must decide whether competition can coexist with love. '
            'Book 4 of The Love Series by Mubarak Ahmad Alibaba.'
        ),
        'genre': 'Romance',
        'tags': ['love', 'rivalry', 'faith', 'Nigeria', 'halal', 'series'],
        'price': 2500,
        'series': 'The Love Series Book 4',
        'tagline': 'Two hearts. One journey... Love, choices, and everything in between.',
        'chapters': [
            ('The Rivalry', 'It began as competition. Two people who wanted the same thing, pursuing it from opposite directions, measuring themselves against each other without acknowledging what they were really doing.\n\nRivalry has a way of creating intimacy. To compete with someone seriously, you must pay attention to them. You must understand how they think. You must, in a way, know them.\n\nAnd knowing someone, truly knowing them, is where love often begins.'),
            ('Tangled', 'I didn\'t plan to become tangled. I thought the boundaries were clear: this person was a rival, not a companion. Someone to compete with, not someone to care about.\n\nBut life rarely respects the categories we create for it. People have a way of becoming more than the roles we assign them — if we let ourselves see them fully.\n\nI began to see her fully. And that changed everything.'),
            ('Two Hearts', 'Two hearts with the same wound heal differently. Two people with the same ambition pursue it differently. And two rivals who begin to feel something unexpected navigate it differently.\n\nWe were learning to navigate. Carefully, cautiously, not quite sure where the line was between competing and connecting, between keeping a safe distance and allowing something real to grow.'),
            ('One Journey', 'The strangest thing about our story is that the rivalry brought us closer than ease ever would have. Easy relationships don\'t require you to know someone deeply. But competition — real, honest competition — demands that you pay attention.\n\nAnd in paying attention to her, I discovered someone worth far more than any victory.'),
            ('Love, Choices, Everything In Between', 'The journey from rivals to something more is not a simple one. It requires choosing, again and again, to see the person beyond the competition. To let your guard down. To decide that connection matters more than winning.\n\nWe made that choice. Imperfectly, slowly, with all the complications that real life brings. But we made it. And the story of how we made it — that is what this book is for.'),
        ],
    },
]

print('Seeding 4 books...\n')

for book_data in BOOKS:
    # Check if already exists
    existing = Story.objects(title=book_data['title']).first()
    if existing:
        print(f'  Already exists: {book_data["title"]}')
        continue

    chapters = []
    for i, (ch_title, ch_content) in enumerate(book_data['chapters'], 1):
        chapters.append(Chapter(
            chapter_number=i,
            title=ch_title,
            content=ch_content,
            created_at=datetime(2026, 8, 23),
        ))

    story = Story(
        title=book_data['title'],
        description=book_data['description'],
        cover_image=book_data['cover'],
        author_id=str(author.id),
        author_username=author.username,
        genre=book_data['genre'],
        tags=book_data['tags'],
        chapters=chapters,
        is_published=True,
        is_completed=False,
        is_premium=True,
        price=book_data['price'],
        free_chapters=3,
        views_count=0,
        likes_count=0,
        created_at=datetime(2026, 8, 23),
        updated_at=datetime(2026, 8, 23),
    )
    story.save()
    print(f'  Created: {book_data["title"]} ({len(chapters)} chapters)')

print('\nDone! 4 books seeded.')
print('Note: Add real chapter content later via the admin panel or by editing this script.')
