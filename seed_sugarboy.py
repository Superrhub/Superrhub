"""
Seeds My Sugar Boy — A Love Too Expensive to Lose
Full 25 chapters from the original novel by Mubarak Ahmad Alibaba
Run: python seed_sugarboy.py
"""
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.users.models import User
from apps.stories.models import Story, Chapter

author = User.objects(username='MubarakAhmedAlibaba').first()
if not author:
    print('Author not found. Run seed_myjannah.py first.')
    exit()

# Delete if exists
existing = Story.objects(title__icontains='Sugar Boy').first()
if existing:
    existing.delete()
    print('Deleted existing Sugar Boy story.')

CHAPTERS = [
    (1, "The Woman in the Black Car",
     """Jayden stared at the balance on his phone for the third time that morning. Three thousand, four hundred and fifty naira. He locked the screen and slipped the phone into his pocket as if hiding the amount could somehow make it larger.

His rent was overdue. His motorcycle needed repairs. His landlord had already reminded him twice that patience was not a substitute for payment. Yet Jayden had never been afraid of hard work. What frightened him was working hard and still remaining exactly where he started.

He dressed in his cleanest shirt and left home determined to find an opportunity. At a small roadside restaurant he met his closest friend, Brian, who joked that Jayden looked like a man going to collect a million naira.

"Maybe today is my lucky day," Jayden replied.

Before Brian could answer, a black Mercedes stopped across the road. A woman stepped out. She was elegant, calm and clearly accustomed to being noticed without asking for attention.

She walked toward them and stopped beside Jayden.

"Excuse me. My name is Vanessa."
"Jayden."
"I know."

He frowned.

"Do you work with computers?"
"A little."

She smiled. "Come to my office tomorrow morning. Ten o'clock."
"For what?"
"An interview. I'll explain when you arrive."

She handed him a business card bearing the name Vanessa Holdings.

"Why me?" Jayden asked.

Vanessa looked at him for a moment. "Because you look like someone who needs an opportunity but is too proud to ask for one."

Then she walked away.

Brian stared after her. "Bro, your life just changed."

Jayden looked at the card again.

He had no idea how right Brian was."""),

    (2, "An Offer He Couldn't Refuse",
     """Vanessa Holdings occupied several floors of a modern building in the heart of the city. Jayden arrived forty minutes early because he could not afford to be late for the opportunity that might change his life.

The receptionist directed him upstairs. Vanessa was waiting.

The interview was unlike any interview Jayden had experienced. Vanessa asked about his education, his computer skills, his failed business ideas and the kind of future he wanted.

"I want to build something of my own," he said.
"What?"
"I don't know yet. Something useful. Something that can employ other people."

Vanessa studied him.

"You think beyond a salary."
"I have to. A salary pays today. A dream is supposed to pay tomorrow."

She smiled.

By the end of the meeting, she offered him a position as a project assistant with a salary far above anything he had previously earned.

Jayden was speechless.

"Are you sure?" he asked.
"I don't make offers I don't mean."

There was one condition: professionalism. Vanessa did not want gossip or personal drama interfering with work.

Jayden agreed.

The first month transformed his life. He paid part of his rent, repaired his motorcycle and helped his mother with expenses. He worked hard and impressed Vanessa with his ability to learn quickly.

Then the invitations began.

Dinner after work. Coffee on weekends. Conversations that had nothing to do with business.

Vanessa asked about his childhood. Jayden asked about her dreams.

One evening she looked across the table and said, "You know, Jayden, money can make life easier. It cannot make loneliness disappear."

He did not know what to say.

Something between them was changing."""),

    (3, "The First Gift",
     """Jayden's first major gift from Vanessa was a phone.

He refused it twice.

"I can't accept this."
"You need it for work."
"I can manage with mine."
"Your phone freezes every time I send you a document."

He laughed despite himself.

Eventually he accepted.

A few weeks later Vanessa helped him replace his unreliable motorcycle with a modest car. She insisted it was not a romantic gift but practical support.

Brian did not believe her.

"Bro, this is how these things start," he warned.
"What things?"
"Today it is a phone. Tomorrow it is a car. Next thing, you are living in a mansion and calling somebody else your boss."

Jayden laughed, but later that night his laughter disappeared.

He looked around his apartment and wondered whether his life was changing because of his own effort or because Vanessa was making it easier.

When he asked Vanessa about it, she said, "I don't want you to feel indebted to me."
"Then why do you keep helping me?"
"Because I want to."

Her answer was simple.

That simplicity frightened him more than a complicated explanation would have.

One evening, after dinner, Vanessa reached for his hand.

"Jayden, do you trust me?"
He looked at her.
"I think I'm learning how."

She smiled.

Neither of them said what they were both beginning to understand."""),

    (4, "Sugar Boy",
     """The nickname began as a joke.

Brian saw Jayden step out of Vanessa's car and laughed.

"Look at Mr. Sugar Boy!"

Jayden rolled his eyes.

But jokes became gossip.

People began whispering that Jayden had found an older wealthy woman to finance his life. Some called him lucky. Others called him a user.

Jayden pretended not to care.

Vanessa cared.

One evening she asked, "Are you ashamed of me?"
"No."
"Then why do you look uncomfortable whenever people see us?"
"Because I don't like people talking."
"They will always talk."

Jayden knew she was right.

Their age difference was obvious. So was the difference in their financial positions.

But there were moments when none of that mattered.

Vanessa could make him laugh when he was exhausted. Jayden could make her forget the pressure of running a company.

Still, one question followed him everywhere:

If Vanessa had no money, would he still love her?

He hated himself for asking it.

He hated himself even more because he could not immediately answer.

One night Vanessa noticed his silence.

"You're thinking too much."
"Maybe."
"About us?"
"Yes."

She squeezed his hand.

"Then think honestly."

Jayden looked at her.

For the first time, he realized love was not going to be simple."""),

    (5, "Rules of the Relationship",
     """Vanessa finally admitted that what existed between them was no longer just friendship or mentorship.

"We need rules," she said.

Jayden smiled. "Rules?"
"Yes."

She counted them on her fingers.

"No lies. No using money to control each other. And if either of us stops wanting this relationship, we say so."

Jayden nodded.

"That sounds fair."

They began spending time together without expensive restaurants or gifts. They watched movies at home, argued about music and laughed over small mistakes.

Jayden discovered that Vanessa hated very sweet tea.

Vanessa discovered that Jayden talked to himself whenever he was nervous.

The more ordinary their relationship became, the more real it felt.

One night Jayden told her, "You're already in my future plan."

Vanessa looked at him carefully.

"Are you sure?"
"Yes."

She kissed his forehead.

But love had a way of becoming complicated precisely when people started believing it was safe."""),

    (6, "Something Real",
     """Vanessa became sick during a stressful week at work.

She told everyone she was fine.

Jayden knew she was not.

He stayed with her, brought food, reminded her to take her medication and cancelled his plans without being asked.

"You don't have to do this," Vanessa whispered.

"I know."
"Then why are you here?"
"Because I want to be."

That was the moment Jayden understood.

He was no longer staying because of the car, the gifts or the opportunities. He was staying because Vanessa mattered.

Vanessa understood something too.

For years people had been attracted to what she could provide. Jayden was the first person in a long time who seemed content simply to sit beside her when she had nothing to give.

Their relationship became deeper.

And because it became deeper, it also became more vulnerable.

Love had entered the room.

Fear followed it."""),

    (7, "The Age Difference",
     """Michelle, Vanessa's older sister, was the first family member to confront her.

"Do you really believe this can last?"

Vanessa was quiet.

"I'm asking because I care about you."

Michelle worried about reputation, the company and the possibility that Jayden might eventually regret choosing a woman older than him.

Meanwhile, Jayden's mother had her own concerns.

"Never allow money to speak louder than your character," she told him.

Jayden promised her he would not.

He later told Vanessa he wanted to become independent.

"I don't want people to say I am with you because of what you have."

Vanessa looked hurt.

"And what do you think?"
"I think I love you."

She held his gaze.

"Then build your own life."

Jayden began saving seriously.

For the first time, the relationship became less about what Vanessa could give him and more about what he could become."""),

    (8, "Whispers",
     """Rumors eventually reached Jayden's mother.

She did not shout. She simply asked one question.

"Are you happy?"
"Yes."
"Are you respected?"

Jayden hesitated.

His mother noticed.

"People's opinions should not control your life," she said. "But you should also never give people reasons to question your character."

Jayden carried those words back to Vanessa.

She listened carefully.

"Your mother is wise."
"She worries."
"So do I."

They agreed to ignore the whispers.

But ignoring gossip was easier than ignoring insecurity.

Every time someone stared, Jayden wondered what they were thinking.

Every time someone praised Vanessa's wealth, he wondered whether they were judging him.

Their love was becoming a battle not only against the world but against the doubts inside themselves."""),

    (9, "Brian Knows",
     """Brian eventually asked the question Jayden had been avoiding.

"If Vanessa disappeared tomorrow, what would you have?"

Jayden became silent.

His apartment. His savings. His skills. A job.

Not enough.

The question forced him to act.

He opened a savings account and began planning a technology company.

Vanessa supported the idea but refused to simply hand him money.

"Build it," she said. "If I invest, I want a proper agreement."

Jayden respected her more for that.

He began spending nights researching, writing business plans and meeting potential clients.

For the first time he felt proud of something that belonged entirely to him.

Vanessa watched his confidence grow.

"You're becoming different."
"Better?"
"More yourself."

Jayden smiled.

But while his future was beginning to take shape, someone from his past was about to return."""),

    (10, "Selena Comes Back",
     """Selena had once been Jayden's serious girlfriend.

Their relationship had ended quietly after years of arguments about money, ambition and the direction of their lives.

When she returned, Jayden was surprised.

They met at a café.

"Are you with someone?" she asked.
"Yes."
"Who?"
"Her name is Vanessa."

Selena nodded.

"Are you happy?"
"Yes."

She smiled sadly.

"Then I wish you well."

The conversation was innocent.

Vanessa did not see it that way.

She saw them together.

That night she asked Jayden who Selena was.

"My past."
"Does she want you back?"
"I don't know."
"Do you?"
"No."

Vanessa nodded, but jealousy had already entered her heart.

And jealousy rarely arrives alone."""),

    (11, "Jealousy",
     """During dinner, Selena called.

Jayden looked at the phone.

Vanessa noticed.

"Are you going to answer?"
"It's probably about the business proposal."
"Then answer."

Jayden stepped outside.

When he returned, Vanessa was quiet.

"You don't trust me," he said.
"I don't trust the situation."
"That is different."
"Is it?"

The argument grew.

Jayden accused Vanessa of trying to control him.

Vanessa accused him of dismissing her fears.

They left separately.

The next morning, neither wanted to apologize first.

Eventually Jayden called.

"I don't want to fight with you."
"Neither do I."

They apologized.

But something had changed.

They had discovered a dangerous truth: love could make them afraid of losing each other, and fear could make them behave like people they did not recognize."""),

    (12, "The First Lie",
     """Selena later invited Jayden to discuss a business partnership.

Jayden knew Vanessa would be uncomfortable.

So he kept the meeting secret.

He told himself he was avoiding unnecessary conflict.

Vanessa found out.

"How did you know?"
"I saw the message."

Jayden could not lie anymore.

"Yes, I met her."
"Why didn't you tell me?"
"Because I knew you'd react like this."

Vanessa stared at him.

"So you protected yourself from my reaction instead of protecting our trust."

Jayden had no answer.

The argument was worse than the first.

Their rule had been simple: no lies.

Jayden had broken it.

Vanessa did not ask him to leave, but she told him she needed space.

For the first time, Jayden wondered whether love could survive a broken promise."""),

    (13, "A Night of Confessions",
     """That night Vanessa finally told Jayden about her past.

Years earlier, a man had loved her while her money was useful. When the money disappeared, so did the love.

"I promised myself I would never be that foolish again," she said.

Jayden listened.

"And now?"
"Now I am scared."

Jayden admitted his own fear.

"People think I'm with you for money."
"Are you?"

The question hurt.

He answered honestly.

"I love you. But I would be lying if I said your money never made my life easier."

Vanessa nodded.

"That is the most honest thing you've said."

They held each other.

Neither promised that fear would disappear.

They only promised not to hide it."""),

    (14, "Money Can't Buy Trust",
     """Jayden returned the car keys.

Vanessa stared at them.

"I don't want to leave you," he said. "I just want to know I can stand on my own."

She respected that.

When he needed funding for his company, Vanessa offered to invest.

This time they signed a formal agreement.

No favors. No hidden expectations. Business was business. Love was love.

For a while, peace returned.

Then a photograph appeared online.

It showed Jayden and Vanessa leaving a restaurant together.

The caption was cruel.

Within hours, thousands of people had seen it.

Vanessa's company board demanded an explanation.

Jayden wanted to fight publicly.

Vanessa wanted silence.

Someone had deliberately taken the photograph.

And someone had deliberately spread it."""),

    (15, "The Photograph",
     """The photograph became the center of a storm.

Board members questioned Vanessa's judgment.

Family members called.

Friends offered opinions nobody had requested.

Jayden was furious.

"Let me tell them the truth."

Vanessa shook her head.

"Public explanations won't make strangers respect us."
"But silence makes us look guilty."
"This isn't about guilt. It's about protecting the company."

Jayden felt pushed aside.

He began wondering whether Vanessa's business would always come before their relationship.

Meanwhile, someone was watching the chaos with satisfaction.

Richard.

Vanessa's former partner.

He believed Jayden had stolen the place that belonged to him.

And he was not finished."""),

    (16, "Her Family Finds Out",
     """Michelle confronted Jayden.

"What exactly do you want from my sister?"

Jayden answered calmly.

"Her trust."

Michelle laughed softly.

"Trust doesn't pay bills."
"I know."
"Then why stay?"
"Because I love her."

Michelle studied him.

Jayden admitted his mistakes.

"I lied about Selena. I accepted things I should have handled differently. But I have never planned to take Vanessa's money and disappear."

Michelle saw something in his face that she had not expected.

Fear.

Not fear of losing money.

Fear of losing Vanessa.

Her attitude softened.

"I hope you're telling the truth."
"So do I."

Sometimes love did not win people over with grand speeches.

Sometimes it won with the simple courage to admit when you were wrong."""),

    (17, "The Price of Love",
     """Vanessa placed a large cheque on the table.

"Take it."

Jayden stared at her.

"What's this?"

"Enough money to start your company somewhere else. Enough to disappear from my life and never worry about money again."

Jayden understood.

She was testing him.

He pushed the cheque back.

"If I take this, you'll always wonder whether I stayed because of money."

Vanessa said nothing.

Jayden tore the cheque.

"I don't want money to decide whether I love you."

Vanessa's eyes filled with tears.

"I've been afraid," she admitted.
"So have I."

They realized they had both been testing each other.

Her test was money.

His test was independence.

Neither had trusted love enough to simply believe it."""),

    (18, "Betrayal",
     """The truth about the photograph finally surfaced.

Brian had accepted money from Richard.

Jayden could hardly believe it.

"You did this?"

Brian looked ashamed.

"I was angry."
"Angry about what?"
"You changed."

Brian admitted that he felt Jayden had forgotten where he came from.

Richard had promised him money in exchange for information.

Vanessa confronted Richard.

"You don't get to decide who I love."

Richard insisted Jayden was using her.

Vanessa refused to listen.

Jayden was hurt by Brian's betrayal more than he expected.

Eventually he forgave him, but forgiveness did not mean returning to the same friendship.

Some doors could be reopened.

Others could only be closed gently."""),

    (19, "Everything Falls Apart",
     """Vanessa decided to step away.

"I need peace," she said.

Jayden wanted to stop her.

But he remembered their promise.

If one person needed space, the other had to respect it.

Vanessa left.

The luxury disappeared.

Jayden moved into a smaller apartment.

For the first time in months, he cooked simple meals, used public transport and focused entirely on his company.

It was difficult.

But every small success felt different.

It belonged to him.

He missed Vanessa.

He missed her voice, her laugh and the way she listened.

Yet he did not chase her with guilt or pressure.

He began to understand that loving someone sometimes meant allowing them to breathe."""),

    (20, "The Empty Apartment",
     """One night Jayden sat alone in his apartment.

There was no expensive furniture. No driver. No luxury. Only silence.

He realized he did not miss Vanessa's money.

He missed Vanessa.

That distinction changed everything.

His company began attracting clients.

He hired his first employee.

Then his second.

The life he had dreamed about was slowly becoming real.

But success did not erase loneliness.

Sometimes after a difficult day, Jayden still reached for his phone to call Vanessa.

Then he stopped.

He wanted her to return because she chose him, not because he had convinced her.

He finally understood that he no longer needed to prove himself to the world.

He only needed to become a man he could respect."""),

    (21, "What She Never Told Him",
     """Vanessa eventually heard that Jayden's company was succeeding.

Michelle told her.

"You were wrong about some things."

Vanessa smiled sadly.

"I know."

She had never told Jayden how deeply afraid she was of being abandoned.

Money had become her armor.

Jayden had made her feel vulnerable again.

She called him.

"Hello."

Neither spoke for several seconds.

"I miss you," she said.

Jayden closed his eyes.

"I miss you too."

They agreed to meet.

Not to restart the relationship.

Just to talk.

But both secretly hoped the meeting would become something more."""),

    (22, "The Last Goodbye",
     """They met at the restaurant where they had once celebrated Jayden's first major promotion.

They spoke honestly.

Jayden admitted he had enjoyed the lifestyle Vanessa provided.

Vanessa admitted she had used money as a shield against emotional insecurity.

They had both made mistakes.

"So what do we do now?" Jayden asked.

Vanessa smiled sadly.

"Maybe we don't go back."

Jayden looked down.

"Then what?"
"We start again."

Slowly.

No expensive gifts. No tests. No lies. No pretending that age, money or public opinion did not matter.

They would acknowledge every difference and choose each other anyway.

It was not a dramatic reunion.

It was better.

It was a mature decision."""),

    (23, "A Different Man",
     """A year later, Jayden's company had grown.

He lived in a comfortable apartment he paid for himself.

He no longer needed to prove that he could survive without Vanessa.

Vanessa was still part of his life, but their relationship had changed.

They went on simple dates.

They discussed problems before they became arguments.

They did not use money to measure love.

One evening Jayden arrived with flowers.

Vanessa smiled.

"You bought these?"
"With my own money."

She laughed.

"Still trying to impress me?"
"No."

He handed them to her.

"Just trying to remind you that I choose you."

Vanessa kissed his cheek.

"And I choose you."

Their love was quieter now.

But it was stronger."""),

    (24, "Years Later",
     """Three years later, Jayden stood on a stage accepting an award for his company.

He looked into the audience.

Vanessa was there. His mother was there. Michelle was there. Even Brian stood at the back, applauding.

Someone shouted, "Sugar boy!"

The room laughed.

Jayden laughed too.

Once the nickname had embarrassed him.

Now it reminded him of how far he had come.

He had learned that being loved by someone wealthy did not make him weak.

Depending on another person for identity did.

After the ceremony, Vanessa walked toward him.

"Congratulations."
"Thank you."
"Ready to go?"

Jayden took her hand.

"Yes."

They walked away together.

Not because she had money.

Not because he needed anything.

Because after everything, they still chose each other."""),

    (25, "My Sugar Boy",
     """They returned to the restaurant where their story had begun.

Jayden looked around and smiled.

"So much happened here."

Vanessa nodded.

"You were different then."
"So were you."

They laughed.

Jayden reached for her hand.

"You know what the greatest gift you ever gave me was?"

Vanessa smiled.

"The car?"
"No."
"The phone?"
"No."
"Then what?"
"You challenged me to become independent."

Vanessa became quiet.

"And you taught me that money cannot buy trust."

They sat together as the evening lights came on outside.

Their story had not been perfect.

There had been jealousy, gossip, betrayal, fear and mistakes.

But love was never about finding two people without problems.

It was about finding two people willing to face their problems honestly.

Vanessa leaned closer.

"My sugar boy."

Jayden smiled.

"Only yours."

And this time, there was no shame in the name.

Because Jayden had finally learned that love was not measured by what one person could give another.

It was measured by what two people were willing to choose, protect and build together.

The End."""),
]

print('Seeding My Sugar Boy...')

chapters = []
for num, title, content in CHAPTERS:
    chapters.append(Chapter(
        chapter_number=num,
        title=title,
        content=content,
        created_at=datetime(2026, 8, 23),
    ))

story = Story(
    title='My Sugar Boy: A Love Too Expensive to Lose',
    description=(
        'Some loves aren\'t meant to be easy... they\'re meant to be worth it. '
        'When Jayden, a young man struggling with bills and broken dreams, '
        'meets Vanessa — a wealthy, elegant woman who sees something in him '
        'that no one else does — their worlds collide in the most unexpected way. '
        'But when money, age difference, jealousy and betrayal enter the picture, '
        'they must answer the hardest question: Is this love real, or just expensive?'
    ),
    cover_image='/static/images/my-sugar-boy.jpg',
    author_id=str(author.id),
    author_username=author.username,
    genre='Romance',
    tags=['love', 'wealth', 'Nigeria', 'romance', 'drama', 'age gap'],
    chapters=chapters,
    is_published=True,
    is_completed=True,
    is_premium=True,
    price=2500,
    free_chapters=3,
    views_count=0,
    likes_count=0,
    created_at=datetime(2026, 8, 23),
    updated_at=datetime(2026, 8, 23),
)
story.save()

print(f'Created: {story.title}')
print(f'Chapters: {len(chapters)}')
print(f'Price: N{story.price}')
print('Done!')
