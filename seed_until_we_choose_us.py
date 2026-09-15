"""
Seeds "Until We Choose Us" by Mubarak Ahmad Alibaba on SuperHub.
Run: python seed_until_we_choose_us.py
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

BOOK = {
    'title': 'Until We Choose Us',
    'cover': '/static/images/until we .jpeg',
    'description': (
        'Some love stories aren\'t meant to be easy, but they\'re worth fighting for. '
        'Adrian and Maya\'s connection begins with a single moment in a café — '
        'but building something real means facing fear, jealousy, rumors, and the '
        'hardest question of all: are you willing to keep choosing each other? '
        'A powerful novel about the love that isn\'t just felt, but decided. '
        'By Mubarak Ahmad Alibaba.'
    ),
    'genre': 'Romance',
    'tags': ['love', 'trust', 'choice', 'romance', 'faith', 'Nigeria'],
    'price': 2500,
    'tagline': "Some love stories aren't meant to be easy, but they're worth fighting for.",
    'chapters': [
        (
            'The Girl Everyone Noticed',
            'The café was louder than usual that afternoon. Cups touched saucers, chairs scraped softly against the floor, and conversations rose and fell like waves. Adrian had come in for coffee and a quiet hour, but the moment he saw Maya, the quiet hour disappeared from his mind.\n\nShe sat near the window with a book open in front of her. She wasn\'t trying to attract attention, yet people noticed her anyway. There was something calm about the way she carried herself, something guarded behind the softness of her expression.\n\nAdrian caught himself looking for the third time.\n\nMaya finally looked up. "Are you planning to say something, or are you just going to keep staring?"\n\nHe smiled. "I was trying to figure out whether you always notice everything."\n\n"Only when someone is making it obvious."\n\nHe laughed, embarrassed but pleased. "Fair enough."\n\nThat simple exchange became a conversation. They spoke about books, music, dreams, and the strange ways people could enter your life without warning. By the time their drinks had gone cold, Adrian had forgotten why he came.\n\nWhen Maya finally stood to leave, Adrian watched her walk toward the door.\n\n"Maybe I\'ll see you again," he said.\n\nShe turned. "Maybe."\n\nAnd somehow, that one word stayed with him long after she was gone.'
        ),
        (
            'A Second Meeting',
            'Two days later, Adrian walked into a bookstore and found himself face-to-face with Maya.\n\nShe raised an eyebrow. "You again?"\n\n"I could ask you the same thing."\n\nShe smiled. "So now you\'re following me?"\n\n"I was about to say the same thing."\n\nThey laughed. The awkwardness of their first meeting had disappeared. Maya helped him choose a novel, teasing him about his taste along the way. When both reached for the same book, their fingers touched.\n\nFor a moment neither moved.\n\nMaya looked away first.\n\n"Sometimes," she said quietly, "the things we think we don\'t need are exactly the things we need."\n\nAdrian studied her face. "Is that advice?"\n\n"Maybe."\n\n"From experience?"\n\nHer smile returned, but it didn\'t reach her eyes. "Maybe that too."\n\nAdrian understood that there was a story behind her smile. He wanted to know it, but he also knew that trust could not be demanded.\n\nOutside the bookstore, they exchanged numbers.\n\nAs Adrian walked away, his phone vibrated.\n\nMaya had already sent a message: "Don\'t get too confident."\n\nHe smiled.\n\n"Too late," he typed.'
        ),
        (
            'Something Real',
            'Their messages began casually. A joke in the morning became a question at night, and soon Adrian found himself checking his phone more often than he wanted to admit.\n\nMaya was careful at first. She answered questions without revealing too much. Adrian didn\'t push. Instead, he let their friendship grow through small moments.\n\nOne evening they walked together after rain had cooled the streets.\n\n"You\'re different when you\'re not trying to impress me," Maya said.\n\nAdrian laughed. "Was I trying?"\n\n"Very hard."\n\nHe shook his head. "And here I thought I was being natural."\n\nShe smiled. Then her expression softened. "I like this."\n\n"This?"\n\n"Us talking without pretending."\n\nAdrian stopped walking. "Then let\'s not pretend."\n\nShe looked at him for a long moment. "Promise?"\n\n"Promise."\n\nNeither knew it yet, but that was the beginning of something real.'
        ),
        (
            'The Past',
            'Maya\'s guardedness became impossible for Adrian to ignore. There were moments when a harmless question could suddenly make her quiet.\n\nOne night, she finally admitted that someone from her past had hurt her badly.\n\n"I learned not to trust promises," she said.\n\nAdrian didn\'t try to defend himself against a history he hadn\'t created.\n\n"I can\'t change what happened before me," he said. "But I can show you who I am now."\n\nMaya looked at him. "That\'s what everyone says."\n\n"Then don\'t believe my words. Watch my actions."\n\nFor the first time, she seemed to believe him a little.'
        ),
        (
            'The Perfect Couple',
            'People began noticing them together. Friends teased them. Strangers assumed they were already a couple.\n\nFrom the outside, everything looked perfect.\n\nBut perfection was never their goal.\n\nMaya could become distant when she was afraid. Adrian could become impatient when he felt ignored. Their first disagreement came over something small, but neither knew how quickly small things could become large when feelings were involved.\n\nThey apologized before the night ended.\n\n"We\'re not perfect," Maya said.\n\nAdrian smiled. "Good. Perfect sounds exhausting."\n\nShe laughed, resting her head briefly against his shoulder.'
        ),
        (
            'A Name From Yesterday',
            'The name Damon appeared unexpectedly.\n\nMaya\'s face changed when Adrian heard it.\n\n"Who is Damon?" he asked.\n\n"Someone I used to know."\n\n"Someone important?"\n\nShe hesitated.\n\n"That depends on what you mean by important."\n\nAdrian didn\'t like the answer, but he trusted her enough not to interrogate her.\n\nStill, the name stayed in his mind.\n\nDamon was no longer just a person from Maya\'s past. He was a shadow standing at the edge of their present.'
        ),
        (
            'Doubt',
            'Adrian tried to ignore the doubts, but doubt was patient.\n\nA delayed reply became a question. A missed call became an explanation he invented himself. He hated the way his mind filled empty spaces with possibilities.\n\nMaya noticed.\n\n"You don\'t trust me."\n\n"I do."\n\n"Then why do you look at me like you\'re waiting for me to disappoint you?"\n\nAdrian had no good answer.\n\nThat night he realized trust wasn\'t simply believing someone. Sometimes it meant refusing to punish them for fears they hadn\'t caused.'
        ),
        (
            'The Confession',
            'Maya finally told Adrian the whole truth about Damon.\n\n"He mattered to me once," she admitted. "But that chapter ended."\n\nAdrian felt jealousy rise, then forced himself to breathe.\n\n"Why didn\'t you tell me earlier?"\n\n"Because I was afraid you\'d see me differently."\n\n"I see you differently," he said. "But not because of Damon. Because now I understand why you\'ve been afraid."\n\nMaya\'s eyes filled with tears.\n\n"I don\'t want to lose you."\n\n"Then don\'t run from me when you\'re scared."\n\nShe nodded.'
        ),
        (
            'Distance',
            'For several days, something between them felt different.\n\nNeither wanted to admit it.\n\nTheir conversations became shorter. Their laughter became less frequent. Adrian wondered whether giving Maya space was the right thing or whether silence was slowly creating a wall.\n\nFinally he called.\n\n"I miss you," he said.\n\nThere was silence.\n\n"I miss you too," Maya answered.\n\nNeither had solved the problem, but both understood that silence could not be their permanent language.'
        ),
        (
            'The Rumor',
            'Then the rumor arrived.\n\nSomeone claimed Maya had secretly met Damon. Another person added details. By the time the story reached Adrian, it sounded like a complete betrayal.\n\nHe confronted Maya.\n\n"I didn\'t meet him," she said.\n\nAdrian wanted to believe her immediately, but anger made everything harder.\n\n"You have to understand why this hurts."\n\n"And you have to understand why being accused hurts me."\n\nThey stood facing each other, both wounded by a story neither had created.'
        ),
        (
            'The Night Apart',
            'That night they stayed apart.\n\nAdrian sat alone, replaying every conversation. Maya lay awake wondering how easily trust could disappear.\n\nNeither slept well.\n\nSometimes love doesn\'t break because people stop caring. Sometimes it breaks because two frightened people stop listening.'
        ),
        (
            'Damon Returns',
            'Damon appeared the next day.\n\nHe told Adrian he had heard the rumor and knew something was wrong.\n\n"I didn\'t meet Maya," Damon said. "And I never told anyone she did."\n\nAdrian stared at him.\n\n"Then who started it?"\n\nDamon shook his head. "That\'s what you need to find out."\n\nFor the first time, Adrian wondered whether the real enemy had never been Damon at all.'
        ),
        (
            'The Truth Behind the Lie',
            'The truth came slowly.\n\nA conversation had been twisted. A message had been taken out of context. Someone had repeated a story without checking it.\n\nMaya had been telling the truth.\n\nAdrian felt ashamed.\n\nHe found her and stood in front of her without excuses.\n\n"I was wrong."\n\nMaya\'s eyes were tired. "You believed the rumor before you believed me."\n\n"I know."\n\n"And that hurt more than the rumor itself."\n\nHe nodded. "I\'m sorry."\n\nThis time, there was no argument.'
        ),
        (
            'Apologies',
            'An apology could not erase the damage, but Adrian stopped trying to make it do that.\n\nInstead, he listened.\n\nMaya told him what the accusation had made her feel. Adrian admitted how fear had controlled him.\n\n"I can\'t promise I\'ll never get jealous," he said.\n\n"I can\'t promise I\'ll never get scared."\n\n"Then we\'ll learn."\n\nShe took his hand.\n\nIt wasn\'t a perfect reconciliation.\n\nIt was an honest one.'
        ),
        (
            'Learning Trust',
            'Trust returned slowly.\n\nAdrian stopped demanding immediate answers. Maya stopped disappearing whenever she felt overwhelmed.\n\nThey created a simple rule: when something hurt, they would talk before assuming.\n\nIt sounded easy.\n\nIt wasn\'t.\n\nBut every difficult conversation they survived became another brick in the foundation of their relationship.'
        ),
        (
            'The Family Question',
            'Marriage entered the conversation unexpectedly.\n\nMaya\'s family wanted stability. Adrian wanted a future with her, but he knew wanting something and being ready for it were different things.\n\n"I don\'t want to rush," Maya said.\n\n"I understand."\n\n"But I also don\'t want us to waste time."\n\nAdrian smiled sadly. "Neither do I."\n\nThey both knew love had to face practical questions eventually.'
        ),
        (
            'Money and Fear',
            'Adrian worried about money.\n\nHe wanted to provide, to build a home, to give Maya the kind of future he imagined for them. But the numbers in his mind never seemed enough.\n\n"What if I\'m not ready?" he asked.\n\nMaya answered gently, "Then we prepare. We don\'t pretend."\n\nHer words relieved something inside him.\n\nMarriage was not a race against another couple. It was a decision two people had to be prepared to carry.'
        ),
        (
            'The Choice',
            'Adrian realized he had been waiting for certainty.\n\nBut certainty rarely arrived before a decision.\n\nHe loved Maya. She loved him. They still had fears, problems, and questions.\n\nMaybe choosing someone didn\'t mean believing life would become easy.\n\nMaybe it meant choosing to face the hard parts together.'
        ),
        (
            'One Last Test',
            'A false message appeared again, designed to make Adrian doubt Maya.\n\nFor a moment the old fear returned.\n\nThen he remembered their promise.\n\nInstead of confronting her angrily, he called.\n\n"Tell me what happened."\n\nMaya explained.\n\nHe listened.\n\nThe test wasn\'t really about the message. It was about whether they had learned from everything that came before.'
        ),
        (
            'The Conversation',
            'They talked for hours.\n\nAbout jealousy. About fear. About Damon. About family. About money. About the future.\n\nMaya cried.\n\nAdrian did too.\n\nNeither tried to win.\n\n"I don\'t want a relationship where we are always defending ourselves," Maya said.\n\n"Then let\'s build one where we feel safe enough to tell the truth."\n\nShe reached for his hand.\n\n"Together?"\n\n"Together."'
        ),
        (
            'No More Secrets',
            'They decided there would be no more hidden chapters.\n\nNot because privacy was wrong, but because secrets built from fear eventually became walls.\n\nMaya shared the parts of her past she had never spoken about.\n\nAdrian shared his insecurities.\n\nFor the first time, neither felt they had to appear stronger than they were.'
        ),
        (
            'The Future',
            'Their future was still uncertain.\n\nBut uncertainty no longer frightened them in the same way.\n\nThey began planning carefully — work, savings, family conversations, and the kind of home they wanted.\n\nTheir dreams were no longer individual pictures.\n\nThey were becoming a shared sketch.'
        ),
        (
            'The Question',
            'Adrian returned to the café where everything had started.\n\nMaya sat by the same window.\n\n"You brought me here on purpose," she said.\n\n"Yes."\n\nHe took a breath.\n\n"I used to think love was finding the perfect person. Now I think it\'s finding someone you\'re willing to choose, even when life isn\'t perfect."\n\nMaya\'s eyes filled with tears.\n\n"Adrian…"\n\nHe reached for her hand.\n\n"Will you choose me?"'
        ),
        (
            'Not Perfect',
            'Maya smiled through her tears.\n\n"We will still argue."\n\n"I know."\n\n"We will still misunderstand each other sometimes."\n\n"I know."\n\n"Life won\'t suddenly become easy."\n\nAdrian smiled. "I know."\n\nShe squeezed his hand.\n\n"Then yes."\n\nThey laughed, cried, and held each other.\n\nIt wasn\'t a perfect ending.\n\nIt was better.\n\nIt was real.'
        ),
        (
            'Until We Choose Us',
            'Years later, Adrian would remember that the beginning had never been perfect.\n\nThere had been fear.\n\nThere had been jealousy.\n\nThere had been rumors, misunderstandings, difficult conversations, and moments when walking away seemed easier.\n\nBut there had also been laughter.\n\nThere had been forgiveness.\n\nThere had been two people learning, slowly, that love wasn\'t simply about how strongly you felt.\n\nIt was about what you did with those feelings.\n\nMaya looked at Adrian and smiled.\n\n"We made it."\n\nHe took her hand.\n\n"No," he said softly. "We chose it."\n\nAnd that was the truth they carried with them.\n\nThey hadn\'t chosen a perfect love.\n\nThey had chosen an honest one.\n\nThey had chosen patience when anger was easier.\n\nThey had chosen conversation when silence felt safer.\n\nThey had chosen forgiveness when pride wanted distance.\n\nMost importantly, they had chosen each other.\n\nAgain and again.\n\nUntil choosing each other became choosing them.\n\nChoosing us.\n\nUntil We Choose Us.'
        ),
    ],
}

print('Seeding "Until We Choose Us"...\n')

existing = Story.objects(title=BOOK['title']).first()
if existing:
    print(f'  Already exists: {BOOK["title"]}')
    print('  Delete it first if you want to re-seed.')
    exit()

chapters = []
for i, (ch_title, ch_content) in enumerate(BOOK['chapters'], 1):
    chapters.append(Chapter(
        chapter_number=i,
        title=ch_title,
        content=ch_content,
        created_at=datetime(2026, 9, 15),
    ))

story = Story(
    title=BOOK['title'],
    description=BOOK['description'],
    cover_image=BOOK['cover'],
    author_id=str(author.id),
    author_username=author.username,
    genre=BOOK['genre'],
    tags=BOOK['tags'],
    chapters=chapters,
    is_published=True,
    is_completed=True,
    is_premium=True,
    price=BOOK['price'],
    free_chapters=3,
    views_count=0,
    likes_count=0,
    created_at=datetime(2026, 9, 15),
    updated_at=datetime(2026, 9, 15),
)
story.save()

print(f'  Created: {BOOK["title"]}')
print(f'  Chapters: {len(chapters)}')
print(f'  Genre: {BOOK["genre"]}')
print(f'  Price: ₦{BOOK["price"]}')
print(f'  Status: Published, Completed, Premium')
print('\nDone! "Until We Choose Us" has been added to SuperHub.')
print('Cover image: static/images/until we .jpeg (already present)')
