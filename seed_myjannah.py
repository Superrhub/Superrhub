"""
Run this script to seed the database with:
  - Author account for Muhammad Mubarak Ahmed
  - Full "My Jannah" story with all 30 chapters

Usage:
    python seed_myjannah.py
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.users.models import User
from apps.stories.models import Story, Chapter
from datetime import datetime


AUTHOR_USERNAME = 'MubarakAhmedAlibaba'
AUTHOR_EMAIL    = 'mubarak@superhub.com'
AUTHOR_PASSWORD = 'MyJannah2024!'
AUTHOR_BIO      = (
    'Muhammad Mubarak Ahmed is a dreamer, a lover of Allah, and a believer '
    'in written words. My Jannah is a piece of his heart — a memory he will '
    'cherish forever.'
)

CHAPTERS = [
    (1, "Before Us",
     """There was a time when I did not know Hauwa would become such an important part of my story. Life was simply moving: ordinary days, ordinary conversations, ordinary plans. I did not know that somewhere in those days, a person would appear and slowly become the name my heart would attach to comfort, happiness, longing, and even pain.

Love rarely announces itself at the beginning. Sometimes it comes quietly. A conversation becomes something you look forward to. A person becomes someone you notice first. Their presence starts changing the atmosphere of your day. Before you know it, you are no longer simply talking to someone; you are building a place for them inside you.

That is how I remember the beginning of us. Not as one dramatic moment, but as a collection of small moments that eventually became one big story.

I would later call her my Jannah. It was not because I believed life with another human being could ever literally be paradise. It was because, in my heart, the name represented what she meant to me: peace, closeness, hope, and a future I wanted to protect.

I did not know where our story would end. I only knew that I wanted to keep turning the pages.

Before Hauwa became a name attached to so many feelings, there was simply ordinary life. That is what makes beginnings difficult to recognize. We usually expect important things to arrive with some announcement, but the people who change us often enter quietly. One conversation becomes another. A familiar name begins to stand out. A presence that once seemed ordinary starts carrying a little more weight.

Looking back, I understand that I was not only discovering another person. I was slowly discovering a different version of myself. I was learning what it felt like to care about someone else's happiness, to look forward to another person's presence, and to imagine that the future might be shared rather than carried alone.

If I could speak to the man I was before all of this, I would tell him to pay attention to the ordinary days. They are often the pages we miss most after they are gone. At the beginning, we think the important part will be the dramatic moments. Later, we realize that the real story was being written in the small ones.

What stays with me most is not a single sentence, but the meaning underneath this chapter. It reminds me that the relationship was made of real people, real feelings, and real choices. I do not want to simplify those experiences. I want to remember them honestly, learn from them, and let the lessons become part of the person I am still becoming."""),

    (2, "Her Name Became Special",
     """Hauwa was no longer just Hauwa to me. Her name slowly became connected to feelings that were difficult to explain.

There are people we meet and forget. There are people we remember because they were kind to us. Then there are those rare people whose presence changes the way we understand our own emotions.

For me, Hauwa became that person.

I started paying attention to the little things: the way she spoke, the way she reacted when she was happy, the moments when she became quiet, and the things she did without realizing how much I noticed them. I learned that love is often built from details.

That was when the name Jannah became mine for her. It was my private way of saying, "You are special to me." Perhaps she did not always understand how deeply I meant it. Sometimes people hear words without hearing the history behind them. But every time I called her my Jannah, I was carrying all the feelings that had grown between us.

Looking back, I wish I had known then how fragile beautiful things can be. When something means everything to you, you naturally believe it will always be there.

We were still writing the early pages. Neither of us knew how complicated the later chapters would become.

There was a point when hearing her name no longer felt neutral. It carried a reaction before I had time to explain the reaction to myself. I noticed the details of her personality, the changes in her mood, and the little habits that made her feel familiar. Familiarity can be a dangerous and beautiful thing: it makes another person feel like part of your world.

The name Jannah became my way of expressing that feeling. It was not a statement that she was flawless. It was a statement about the place she occupied in my heart. The name carried tenderness, hope, and a kind of private meaning that words like 'girlfriend' or 'friend' could never completely capture.

Perhaps one of the lessons in giving someone a special name is that names collect memories. The more life you share, the more meaning a name can carry. Eventually, one word can contain entire seasons of your life."""),

    (3, "The Little Things",
     """Our relationship was not made only from big promises. It was made from small things.

A conversation. A look. A laugh. A disagreement that ended with understanding. A moment when one of us needed the other. The simple comfort of knowing someone was there.

Those moments became memories before I even realized I was collecting them.

I think that is one of the reasons losing peace between two people hurts so much. You are not only missing a person. You are missing hundreds of small experiences that became part of your everyday life.

With Hauwa, ordinary moments could feel important because she was there.

I began to understand that love is not always loud. Sometimes love is checking whether someone has eaten. Sometimes it is staying awake when you should be sleeping because you want to hear their voice. Sometimes it is forgiving something that hurt you because you know the person matters more than the argument.

I did not get everything right. I know that now.

But I loved her in the way I knew how at the time. Sometimes that love came out imperfectly. Sometimes I said the wrong thing. Sometimes I misunderstood. Sometimes I expected her to understand what was inside my heart without explaining it properly.

That is one of the hardest lessons our story gave me: loving someone deeply does not automatically mean you know how to love them perfectly.

The little things were easy to overlook while they were happening because they did not look important. But relationships are rarely built from grand moments alone. They are built from repetition: checking in, listening, laughing, remembering, forgiving, and showing up again.

The little things deserve more respect than I gave them at the time. They were not interruptions between the important moments; they were the important moments. A relationship is experienced mostly in ordinary time. That is why memories of simple conversations and small acts can become so powerful later. They remind us that love was not only something we promised. It was something we practiced."""),

    (4, "When Love Became Real",
     """There was a point when I stopped thinking of us as something temporary.

Hauwa had become part of the way I imagined tomorrow.

When you reach that point, your thoughts change. You start thinking beyond today's happiness. You begin asking questions about the future, responsibilities, family, stability, and whether two people can build a life together.

That kind of love can be beautiful, but it can also be frightening because suddenly there is something important to lose.

I wanted our story to become stronger, not weaker. I wanted the difficult days to become lessons instead of endings.

I also learned that two people can love each other and still misunderstand one another. Love does not remove human weakness. It only makes the consequences feel bigger.

Every disagreement carried more weight because I cared.

Every cold moment felt longer because I remembered the warmth that came before it.

And every time things became peaceful again, I was grateful.

I wish I could return to some of those days with the wisdom I have now. I would speak more carefully. I would listen more. I would not assume that love gives me permission to overlook her feelings.

But life does not let us rewrite yesterday. It only gives us today to learn from it.

What I understand now is that love needs more than strong feelings. It needs skills. Listening is a skill. Apologizing is a skill. Giving space is a skill. Explaining yourself without attacking the other person is a skill. I was still learning all of them.

When love became real, I also became more aware of what could be lost. That awareness made me hopeful, but it also made me vulnerable. I wanted certainty because certainty felt like safety. I had to learn that a healthy relationship cannot be protected by fear. It is protected by honesty, patience, and the willingness to keep learning each other."""),

    (5, "The Man I Was Becoming",
     """Loving Hauwa made me think seriously about the man I wanted to become.

I began thinking about responsibility. About money. About stability. About family. About the kind of future a woman would deserve if she trusted me with her heart.

I wanted to be capable of carrying responsibilities, not merely promising that I could.

Sometimes that pressure made me emotional. Sometimes it made me afraid. And sometimes, instead of explaining that fear properly, I communicated it badly.

That is something I regret.

There are moments when a man is carrying many thoughts inside himself, but the woman he loves only sees the words that come out. She cannot automatically see the pressure behind them.

I wanted Hauwa to understand me, but I also needed to understand her. Love requires two people to translate their hearts for each other.

I was still learning that language.

I was still learning how to balance love with responsibility, emotion with patience, and family expectations with personal desires.

Hauwa did not create all of those struggles, but our relationship became the place where many of my hopes and fears met.

That is why what happened between us affected me so deeply.

I wanted to become dependable, not merely romantic. I wanted my words about the future to have substance behind them. I wanted to become a man whose promises had weight. That desire was sincere, but I learned that responsibility is not only about what we carry privately. It is also about how clearly we communicate what we are carrying. If I am worried, the person I love should not have to guess. If I am preparing for the future, I should explain that preparation with reassurance rather than allowing it to become distance."""),

    (6, "The First Cracks",
     """Every relationship has moments when something changes.

Sometimes it is one argument. Sometimes it is a series of small disappointments that slowly build into distance.

For us, misunderstandings began to matter more.

A sentence could be interpreted differently from how it was intended. Silence could be mistaken for indifference. A delayed call could become a question about love. A disagreement could become evidence that the other person no longer cared.

Looking back, I understand that many relationship problems are not caused by a lack of love. They are caused by two hurt people trying to protect themselves at the same time.

I was protecting my feelings.

She was protecting hers.

And somewhere between those two defenses, we stopped hearing each other clearly.

I wish I had slowed down more often.

I wish I had asked, "What did you mean?" before assuming.

I wish I had remembered that winning an argument is not the same thing as protecting a relationship.

Our story was entering a difficult chapter, but I still believed we could find our way back.

I still believed that love could teach us how to repair what pride and misunderstanding had damaged.

The first cracks taught me how quickly two people can move from trying to be understood to trying to defend themselves. Once that happens, even good intentions can become difficult to hear. I wish I had recognized sooner that protecting the relationship sometimes means protecting the conversation itself. The goal should be understanding, not victory."""),

    (7, "The Silence",
     """There were days when silence became louder than conversation.

Not hearing from Hauwa felt strange because I had become used to her presence. When someone becomes part of your routine, their absence can feel like a missing piece of the day.

I started thinking too much.

I replayed conversations. I remembered words. I wondered what she was feeling. I wondered whether she still cared.

Sometimes the mind creates answers when the heart does not have enough information.

That is dangerous.

I began realizing how quickly fear can turn uncertainty into certainty.

If she was quiet, my mind could say she was done.

If she was distant, my mind could say she no longer loved me.

But silence does not always tell the whole story.

I wish we had been better at talking before silence became our language.

Still, even in those difficult moments, my feelings did not disappear.

If anything, the distance showed me how deeply attached I had become.

I did not want to lose her.

I did not want our story to become something we only remembered.

I learned that uncertainty is uncomfortable, but discomfort is not proof. A quiet phone does not automatically explain why someone is quiet. A delayed answer does not automatically define the value of a relationship. I wish I had been better at leaving space for facts instead of allowing fear to complete the story."""),

    (8, "The Words We Could Not Take Back",
     """Arguments have a strange power. In the moment, people speak from pain, anger, fear, or frustration. Later, they may wish they had chosen different words.

We had moments like that.

I know I said things I would express differently today. I know there were moments when my emotions were stronger than my wisdom.

For that, I am sorry.

Not because I want to pretend that only one person made mistakes, but because I can only take responsibility for my own side.

I cannot control what Hauwa felt. I cannot rewrite what she heard. I cannot force her to forget what hurt her.

What I can do is acknowledge my part.

I am sorry for the moments I made her feel unheard.

I am sorry for the times I reacted instead of understanding.

I am sorry for the moments when my love became mixed with fear of losing her.

A sincere apology is not supposed to be a tool for forcing someone to return. It is supposed to be the truth spoken without conditions.

And my truth is simple: I made mistakes. I hurt someone I loved. And I wish I had handled some things better.

An apology becomes meaningful when it does not come with a hidden demand. I do not want to say sorry in order to purchase forgiveness or to make reconciliation unavoidable. I want the apology to stand on its own: I was wrong in those moments, you were hurt, and I wish I had chosen differently.

Words spoken in pain can remain long after the emotion has passed. What I can do is learn from the effect my words had and become more careful with the next ones. An apology becomes real when it changes the person who is apologizing."""),

    (9, "My Jannah",
     """There is a reason I called her my Jannah.

It was never just a nickname.

It carried affection. It carried hope. It carried the picture I had of a future where two people who loved each other could build something peaceful.

When I said "my Jannah," I was saying that she had become precious to me.

Maybe the name became even more meaningful because of what happened later.

When things are easy, it is easy to call someone beautiful names.

When things become painful, those names become memories.

I still remember what it felt like to say it with happiness.

And now the same name carries longing.

That is the strange thing about love: the same memory can make you smile and hurt you at the same time.

I do not regret loving her.

I regret the parts of the journey where we failed to protect the love we had.

If I could explain the name to her one more time, I would tell her that I never meant it as a claim of ownership.

She was never something I owned.

She was someone I cherished.

There is a difference.

The name Jannah carried my hope for peace, closeness, mercy, and companionship. It also became a reminder that love should never become ownership. To call someone precious is not to possess them. It is to recognize their value while respecting their freedom. That distinction matters deeply to me now."""),

    (10, "The Day Everything Felt Different",
     """There came a point when I realized that things were no longer the same.

Hauwa began creating distance.

The person I wanted close to me was now asking for space in a way that I found difficult to accept.

She spoke about being friends.

Those words were painful because my heart was not standing in the same place.

I could not simply turn off my feelings because the relationship had changed.

The hardest part was being close physically while feeling far away emotionally.

Sometimes the person you miss is not far from you. They can be nearby, yet unreachable.

That kind of distance is its own form of heartbreak.

I wanted to fix everything immediately.

But I learned that you cannot repair a heart by forcing it.

Love needs consent.

Healing needs space.

And reconciliation, if it ever comes, has to be chosen by both people.

That realization did not make the pain disappear. It only taught me that love sometimes means stepping back even when every part of you wants to hold on.

The day everything felt different was painful because the change was not only in circumstances. It was in the meaning I attached to ordinary moments. I had to learn that another person's need for space is not automatically a judgment of my worth. Sometimes the healthiest response to distance is not another attempt to close it, but the patience to let both people breathe."""),

    (11, "The Night She Cried",
     """One of the moments I will remember is seeing Hauwa cry.

Whatever had happened between us, seeing her in pain changed something inside me.

I did not want to be the reason she suffered.

There are moments when arguments become meaningless because you suddenly see the person behind the disagreement.

She was not an enemy.

She was someone I loved.

I tried to be there for her. I took her home and made sure she was okay.

That moment reminded me of something important: even when a relationship is broken, compassion should not disappear.

Love should never become an excuse to punish someone.

If I ever loved Hauwa, I had to care about her wellbeing even when I was hurting too.

That night did not solve our problems.

But it became one of the moments that stayed with me.

It showed me that behind all the words, there were two human beings who had both been affected by what was happening.

And sometimes, the person standing in front of you is not asking you to win.

They are asking you to understand.

Seeing someone you love in pain can strip away the arguments that seemed so important before. In that moment, compassion becomes more important than being understood. I learned that caring for someone does not disappear simply because the relationship is difficult. If anything, difficult moments reveal whether our care was only about getting what we wanted or whether it included genuinely wanting the other person to be okay."""),

    (12, "Breakfast",
     """The morning after a difficult night, I made breakfast for her.

It was a small thing.

But sometimes small things say what words cannot.

I could not fix everything with food. I could not erase the misunderstanding. I could not make her feelings change.

But I could still care.

Making breakfast reminded me that love is often expressed through ordinary acts.

A plate of food.

A glass of water.

Asking whether someone slept.

Sitting quietly nearby.

The problem was that I wanted those little acts to lead us back to where we were.

But sometimes kindness is simply kindness. It cannot be used as a bridge to force someone into a decision.

That was another lesson I had to learn.

I could show love without demanding an outcome.

I could apologize without demanding forgiveness.

I could care without demanding closeness.

And if I truly wanted the best for Hauwa, I had to learn that distinction.

Breakfast was a small act, but it represented something larger in my mind: care that did not require a speech. There are moments when the best thing you can do is simply make life a little easier for another person. Yet I also had to learn not to turn kindness into a bargain. Care loses some of its goodness when it becomes a hidden transaction. I wanted to love without using love as leverage. I wanted my actions to be sincere even if they did not produce the outcome my heart wanted."""),

    (13, "Just Friends",
     """Then came words that were difficult for me to hear: "We are just friends."

For someone whose heart was still deeply attached, friendship did not feel simple.

How could I suddenly place all those memories into a smaller box and call them friendship?

How could I see the same person and pretend my feelings had disappeared?

I could not.

At least, not immediately.

I understood that Hauwa had the right to define what she wanted.

But I also had the right to acknowledge what I felt.

That is why the situation became so painful.

Two truths could exist at once.

She could want distance.

And I could still love her.

She could need friendship.

And I could need time to heal.

Neither truth automatically made the other person wrong.

I began understanding that sometimes love does not end at the same speed for both people. One heart may still be holding on while the other is already trying to let go.

That difference can be heartbreaking.

But it is real.

I learned that respecting someone does not require pretending you feel nothing. I could acknowledge my attachment honestly while also acknowledging her right to choose. That balance was painful, but it was healthier than trying to deny either truth.

Sometimes the kindest thing is to admit that friendship may not be immediately possible for a heart that is still healing. Time can create clarity. Distance can create emotional stability. Neither has to be an act of punishment."""),

    (14, "The Compound",
     """Being close to someone after a breakup is different from leaving them behind.

Hauwa was not some distant person I could simply avoid forever.

We were in the same compound, close enough for everyday life to keep reminding me.

A door.

A hallway.

A passing moment.

A familiar presence.

Sometimes healing requires distance, but life does not always give us perfect distance.

So I had to learn another kind of strength: how to control my reaction when I saw someone my heart still wanted.

I had to learn not to chase every moment.

Not every silence needed an explanation.

Not every glance needed interpretation.

Not every day needed a conversation about the relationship.

I was learning to give both of us room to breathe.

It was difficult.

But I began to understand that love without boundaries can become pressure.

And I never wanted my pain to become pressure on her.

Boundaries became a form of respect. They were not proof that love had disappeared. They were proof that love could exist without becoming pressure.

I learned that maturity is sometimes quiet. It is not reacting to every encounter, not turning every glance into a message, and not forcing every moment to answer the question of what we are. Space can be a form of respect when it is given without punishment."""),

    (15, "My Heart Still Says Her Name",
     """Even when I tried to act strong, my heart still remembered her.

That is the part people do not always understand about heartbreak.

You can know what you should do and still feel something completely different.

Your mind can say, "Give her space."
Your heart says, "Go and talk to her."

Your mind says, "Let time work."
Your heart says, "Fix it tonight."

Your mind says, "Accept what she has chosen."
Your heart says, "But what about everything we had?"

I lived inside that conflict.

Some days I felt hopeful. Other days I felt empty. Some days I wanted to fight for us. Other days I wanted to disappear from the situation completely.

But slowly, I realized that healing is not about winning the argument between your heart and your mind.

It is about allowing both to speak while choosing what is healthy and respectful.

My feelings were real.

But so were her boundaries.

Both mattered.

I stopped treating my feelings as commands. Feeling the urge to reach out did not mean I had to reach out. Missing someone did not mean I had to interrupt their space. Hope did not mean I had to demand an answer.

That was a quiet kind of strength: allowing the feeling to exist without allowing it to control my behavior. I could miss her and still respect her. I could love her and still work on myself.

Feelings are real, but they do not always have to become actions."""),

    (16, "My Apology",
     """So I say this from my side:

Hauwa, I am sorry.

I am sorry for the things I did that hurt you.

I am sorry for the moments I made you feel misunderstood.

I am sorry for the times my emotions spoke louder than my patience.

I am sorry for every situation where I could have chosen peace and did not.

I am not writing this to prove that I was right.

I am writing it because I know I was not perfect.

I cannot ask you to forget your feelings.

I cannot demand that you return.

I cannot force the past to become different.

But I can be honest about my mistakes.

If there is anything I want you to know, it is that my love was never meant to become a burden to you.

I wanted to be someone who brought peace into your life.

Where I failed at that, I take responsibility.

And if someday you remember me, I hope you remember that beneath all my mistakes was a man who genuinely cared about you.

My apology became more honest when I stopped thinking about what it might produce. I could not use regret as a bargaining tool. I could only acknowledge what I had done, accept that she had her own experience of it, and commit myself to learning. The apology matters because it tells the truth, not because it guarantees reconciliation."""),

    (17, "What We Taught Each Other",
     """Every relationship teaches something.

Hauwa taught me that love requires patience.

She taught me that words have weight.

She taught me that people can be hurting even when they are not saying it.

She taught me that affection alone is not enough.

A relationship needs communication.

It needs trust.

It needs emotional safety.

It needs two people willing to repair things after conflict.

I hope I taught her something too.

Maybe that she was deeply valued.

Maybe that someone could care about her happiness even when things were difficult.

Maybe that she was loved in a way that was sincere, even if imperfect.

Our relationship was not perfect.

But perfection is not what makes a story meaningful.

Sometimes the imperfect chapters teach the deepest lessons.

I also learned that affection cannot substitute for trust. Saying 'I love you' cannot repair every misunderstanding. Sometimes the repair requires changed habits, consistent patience, and the humility to admit that the other person experienced a situation differently.

The lessons of a relationship do not belong only to the good days. Some of the deepest lessons come from the moments when communication failed. I learned that love needs skills: listening, patience, repair, emotional safety, and accountability. These are not abstract ideas. They are habits that have to be practiced when emotions are strongest."""),

    (18, "The Future I Imagined",
     """There was a future I once imagined.

It had us in it.

I imagined ordinary mornings, shared responsibilities, laughter, arguments that ended in forgiveness, and the comfort of knowing that after a difficult day there was someone waiting at home.

I imagined growing together.

I imagined becoming better people because of each other.

That future may still exist in some form, or it may not.

That uncertainty is one of the hardest parts.

But I have learned not to confuse a dream with a guarantee.

A future with another person must be chosen by both people.

I cannot build it alone.

So I release the need to control the ending.

I can still hope.

But I must also respect reality.

If our paths meet again with healthier hearts, perhaps there will be another chapter.

If they do not, then I will still be grateful for the chapters we had.

The future I imagined was powerful because it had become emotionally real before it became physically real. I had pictured ordinary life, responsibility, laughter, and companionship. I learned that imagining a future is different from being promised one. A shared future requires two people choosing it together, repeatedly, with open eyes.

So I am learning to hold dreams differently. I can hope without insisting. I can pray without demanding. I can prepare myself for a good future without deciding who must be in it."""),

    (19, "Love and Responsibility",
     """Love made me think about responsibility in a way I had never understood before.

It is easy to say, "I love you."

It is harder to become the kind of person who can carry what those words require.

There are financial responsibilities.

Family responsibilities.

Emotional responsibilities.

Promises.

Decisions.

Patience.

Sacrifice.

I wanted to prepare myself properly for the responsibilities of marriage and adulthood. I did not want to make promises without being ready to carry them.

Sometimes that desire for preparation could look like uncertainty.

But inside me, it was fear of failing the person I loved.

I wanted to be ready.

I wanted stability.

I wanted to know that when I said "I will take care of us," I had worked hard enough to make those words meaningful.

Love made responsibility feel real. It was no longer enough to say that I wanted a future; I had to think about whether I was becoming capable of sustaining one.

There is a difference between wanting to provide and being prepared to provide. There is a difference between promising stability and building the habits that create stability. I was learning that love is partly preparation for responsibility.

Love and responsibility cannot be separated for long. I wanted stability not because my feelings were weak, but because I wanted my feelings to survive real life. That remains one of the most important lessons I take from this story."""),

    (20, "When I Wanted to Hold On",
     """There were moments when every part of me wanted to hold on.

I wanted to tell Hauwa that what we had was too beautiful to lose.

I wanted to remind her of the beginning.

I wanted to tell her about all the moments that made me call her my Jannah.

I wanted to ask her not to let one painful chapter erase the whole story.

But I also learned that reminding someone of beautiful memories cannot force their heart to change.

So I began changing the way I held on.

Instead of holding on to her decisions, I held on to respect.

Instead of holding on to control, I held on to prayer.

Instead of holding on to constant contact, I held on to patience.

That was harder than chasing.

But it was healthier.

Sometimes the strongest way to love someone is to stop trying to control the outcome.

Holding on used to mean trying to preserve the relationship by force of effort. Slowly, I learned another definition. Sometimes holding on means holding on to your values when you cannot hold on to the person.

I could hold on to respect. I could hold on to prayer. I could hold on to the lessons. I could hold on to gratitude for what had been good. Those things were within my control.

When I wanted to hold on, I had to learn what holding on could mean without becoming pressure. I did not have to hold another person tightly in order to prove that I cared. Sometimes love becomes healthier when it releases control."""),

    (21, "The Prayer",
     """There were nights when I did not know what else to do except pray.

I asked Allah to calm my heart.

I asked Allah to guide me.

I asked Allah to protect Hauwa.

And I asked for whatever outcome was truly best for both of us.

Sometimes I prayed for us to find our way back.

Other times I prayed for the strength to accept whatever Allah had written.

That change in prayer was important.

At first, I wanted a specific answer.

Later, I wanted peace.

There is a difference.

When you love someone deeply, surrendering the outcome can feel like giving up.

But faith taught me that surrender is not the same as hopelessness.

It is trusting that what is meant for you will not pass you by, and what is not meant for you cannot be held forever by force.

So I placed our story before Allah.

Not because I stopped caring.

Because I cared enough to ask for what was best.

Prayer became the place where I could bring feelings that I did not know how to organize. I could admit that I wanted her, that I was afraid, that I hoped, and that I did not know what would happen.

Faith gave the story a different ending even before I knew the actual ending. Whatever happened between us, I did not want heartbreak to become a reason to lose hope in Allah's wisdom.

At first I wanted a particular answer. With time, I began asking for what was best, even when I did not know what that would look like. That shift was not a loss of hope. It was a deeper form of trust."""),

    (22, "The Things I Would Do Differently",
     """If I could go back, I would listen more.

I would ask questions before assuming.

I would explain my feelings without turning them into accusations.

I would give her room to speak.

I would recognize that being right is not always more important than being gentle.

I would protect our private moments from unnecessary pressure.

I would not let fear of losing her make me behave in ways that could push her further away.

Most importantly, I would remember that love is not only about how strongly I feel.

It is also about how safely the other person experiences that love.

That is a lesson I will carry with me whether our story continues or not.

The things I would do differently are not a list of regrets meant to punish myself. They are lessons I want to carry forward. Regret is useful only when it becomes instruction.

I would listen before defending myself. I would explain before assuming I had been understood. I would recognize that reassurance can be given without surrendering dignity, and boundaries can be respected without treating them as rejection.

Most importantly, I would measure love not only by how strongly I feel but by how safe the other person feels around that love. That is a standard I want to keep.

If regret becomes wisdom, then even painful memories can produce something useful."""),

    (23, "If We Ever Find Our Way Back",
     """If we ever find our way back to each other, I do not want us to return to exactly who we were.

I would want something better.

A relationship where we speak before resentment grows.

Where apologies are followed by changed behavior.

Where boundaries are respected.

Where family and future responsibilities are discussed with honesty.

Where love is not measured by how much we suffer for each other, but by how well we care for each other.

If there is another chapter, I want it to be written by two wiser people.

Not two people pretending nothing happened.

Two people who remember what happened and choose to grow from it.

If our paths ever meet again, I would not want us to pretend the difficult chapter never happened. I would want us to understand it. A return without growth would only repeat the same patterns.

A healthier relationship would need conversations that happen before resentment becomes permanent. It would need apologies followed by behavior that demonstrates change. It would need room for both people to speak honestly.

If there is another chapter, I hope it is built slowly. Not from fear of losing each other, but from trust that does not require constant proof."""),

    (24, "If This Is Where Our Story Ends",
     """There is another possibility I have had to face.

What if this is where our story ends?

It hurts to write that sentence.

But a love story does not become meaningless because it does not last forever.

Some people change us through staying.

Others change us through leaving.

Hauwa changed me.

She showed me how deeply I could care.

She showed me my weaknesses.

She showed me the parts of myself I still needed to grow.

For that, I will always be grateful.

If our final chapter is separation, I hope it is not filled with hatred.

I hope it is filled with gratitude for what was good and wisdom about what went wrong.

I hope we both find peace.

Accepting the possibility of an ending is not the same as saying the relationship did not matter. In fact, sometimes acceptance is how we honor what mattered without turning it into a lifelong wound.

If this is where the story ends, I do not want the ending to become a verdict on everything that came before it. A relationship can be meaningful even when it does not last forever. I want to remember what was beautiful without denying what was painful, and I want both of us to move forward without needing to make the other person a villain."""),

    (25, "The Man After Hauwa",
     """Whatever happens, I know I cannot remain the same person.

I have learned that love needs maturity.

I have learned that communication matters.

I have learned that apologies are meaningful only when behavior changes.

I have learned that another person's freedom must remain intact even when your feelings are strong.

And I have learned that heartbreak does not mean your life is over.

There is still work to do.

There are still dreams.

There is still family.

There is still faith.

There is still a future.

Hauwa may always have a special place in my history.

But I must also build a healthy future for myself.

The man after Hauwa has to be more than the man who misses Hauwa. He has to be someone who learned from loving her. Otherwise, the pain would remain only pain.

I want to become more patient in communication, more disciplined in responsibility, and more respectful of boundaries. These lessons are not useful only if the relationship returns. They are useful because they belong to the person I am becoming.

Hauwa may remain an important part of my history without becoming the definition of my entire future. I can carry gratitude and continue building a life that is healthy, purposeful, and faithful.

Growth is one way of honoring what mattered."""),

    (26, "The Memories",
     """There are memories I will keep quietly.

The conversations.

The laughter.

The moments when everything felt simple.

The times I called her my Jannah.

The moments when we needed each other.

Even the painful memories have something to teach me.

I will not pretend every moment was perfect.

But I also will not allow the ending to erase the beginning.

What was beautiful was beautiful.

What was painful was painful.

Both can be true.

That is how real relationships work.

They are made of many truths at once.

Memories do not ask permission before returning. A song, a familiar phrase, a quiet moment, or a simple thought can bring back an entire season of life. I have learned not to fight every memory.

Instead, I can let the memory exist without turning it into a reason to reopen every wound. I can remember something beautiful and say, quietly, 'That mattered.' I can remember something painful and say, 'That taught me.'

The goal is not to erase the past. The goal is to place the past where it belongs: behind me, respected but no longer controlling the direction of my life."""),

    (27, "A Letter Inside the Book",
     """Hauwa,

If you ever read these pages, I hope you understand that I did not write them to pressure you.

I wrote them because you mattered.

You became a chapter of my life that I could not summarize in a few sentences.

I am sorry for my part in the pain between us.

I am sorry for the moments I could have done better.

I am grateful for the moments you gave me.

And I pray that Allah gives you peace, happiness, protection, and a future filled with goodness.

I do not know what tomorrow will bring.

But I know what I feel today: I cared for you deeply. I still care.

And I hope whatever happens, we both become better people because our paths crossed.

If Hauwa ever reads these pages, I hope she reads them without feeling responsible for my emotions. This book is not a request that she carry my heart for me. It is simply an honest record of what the relationship meant from my side.

I want the apology to remain an apology, not a negotiation. I want the gratitude to remain gratitude, not a hidden request. And I want the prayer for her happiness to be sincere whether or not our paths become close again.

Whatever she remembers, I hope she knows that she was not insignificant. She mattered enough to change the way I think about love, responsibility, communication, and myself."""),

    (28, "Our Story Is More Than the Ending",
     """People often judge a relationship by how it ends.

I do not want to do that.

Our story was more than the final disagreement.

It was more than the silence.

More than the tears.

More than the words "just friends."

It was also the beginning.

The laughter.

The affection.

The hope.

The ordinary days that became memories.

The love that made two people imagine a future together.

That is why I refuse to call everything a mistake simply because things became difficult.

Some things were real even if they did not last forever.

And some lessons are valuable precisely because they came through pain.

Our difficult ending cannot make every earlier moment false. The good was good. The painful was painful. Both belong to the truth.

I want to resist the urge to rewrite the entire story based on its final pages. Sometimes the most honest conclusion is simply that something meaningful happened, it became difficult, and it changed the people who lived it.

Our story is more than its ending because people are more than the final moment between them. There were beginnings, laughter, affection, hope, mistakes, and lessons. The truth can hold beauty and pain at the same time."""),

    (29, "Jannah 🤍",
     """If there is one name I will remember from this chapter of my life, it will be Jannah.

Not because I believe a person can be perfect.

But because the name became a symbol of what I hoped love could be.

Peace.

Home.

Companionship.

Mercy.

Forgiveness.

A future.

Hauwa, you were the person behind that name.

Whatever the future decides, I hope you know that the name came from a place of genuine affection.

You were not just another person I dated.

You became part of my story.

And some stories stay with us because they changed the person who lived them.

Jannah became more than a nickname because it gathered a meaning around itself. It came to represent the kind of peace and companionship I hoped to build with someone.

But perhaps the deepest lesson is that the qualities I attached to the name are also qualities I must learn to create within myself: peace, mercy, patience, responsibility, and faith.

So when I remember the name, I do not want only to remember what I lost. I want to remember what I hoped to become. In that sense, the name can continue to teach me.

Jannah became a symbol for the qualities I hoped love could contain: peace, mercy, companionship, forgiveness, and a future built with care. Remembering the name can remind me not only of a person, but of the kind of man I want to become. I want to create those qualities in my own life rather than only searching for them in someone else."""),

    (30, "The Last Page Is Not Necessarily the End",
     """This is the last page of this book, but it does not have to be the last page of the story.

Maybe there will be another chapter.

Maybe there will not.

I cannot promise the future.

But I can promise myself something: I will learn.

I will become more patient.

I will communicate better.

I will take responsibility for my mistakes.

I will respect the choices of the person I love.

And I will keep my faith in Allah.

Hauwa, my Jannah 🤍, thank you for the part of my life you shared with me.

If our paths meet again, I hope we meet as wiser people.

If they do not, I hope we both walk forward without bitterness.

I will remember the beginning with gratitude, the middle with humility, and the ending with acceptance.

Because sometimes love is not only about keeping someone.

Sometimes love is also about becoming a better person because you once had the privilege of loving them.

And that is where I leave our story for now:

Not with hatred.

Not with blame.

But with a prayer.

May Allah guide us, heal us, and write what is best for both of us.

— Muhammad

The last page is not necessarily the end because I do not know the future. What I can decide is how I leave this chapter. I can leave without hatred. I can take responsibility without destroying myself with regret. I can keep faith without demanding a particular answer. Whatever happens next, I want the lessons of this story to continue shaping the life I live."""),
]


def seed():
    print("🌱 Seeding SuperHub database...")

    # Create or get author
    author = User.objects(username=AUTHOR_USERNAME).first()
    if not author:
        print(f"  Creating author: {AUTHOR_USERNAME}")
        author = User(
            username=AUTHOR_USERNAME,
            email=AUTHOR_EMAIL,
            bio=AUTHOR_BIO,
        )
        author.set_password(AUTHOR_PASSWORD)
        author.save()
        print(f"  ✅ Author created — login: {AUTHOR_EMAIL} / {AUTHOR_PASSWORD}")
    else:
        print(f"  ℹ️  Author already exists: {AUTHOR_USERNAME}")

    # Check if story exists
    existing = Story.objects(
        author_id=str(author.id), title__icontains='My Jannah'
    ).first()

    if existing:
        print(f"  ℹ️  Story already exists: {existing.title}")
        print("  Use --force flag to re-seed.")
        return

    # Create story
    print("  Creating 'My Jannah' story...")
    chapters = []
    for num, title, content in CHAPTERS:
        chapters.append(Chapter(
            chapter_number=num,
            title=title,
            content=content,
            created_at=datetime(2024, 1, num if num <= 28 else 28),
        ))

    story = Story(
        title='My Jannah: The Story of Hauwa and Me',
        description=(
            'Some stories are written by fate, but ours was written by Allah. '
            'A deeply moving true story of love, faith, misunderstandings, growth, '
            'and the lessons that shaped a man. From the very first conversation to '
            'countless memories — this is the journey of Mubarak and Hauwa. '
            '"A True Story. A Pure Love. A Beautiful Journey."'
        ),
        cover_image='',
        author_id=str(author.id),
        author_username=AUTHOR_USERNAME,
        genre='Romance',
        tags=['love', 'faith', 'Nigeria', 'halal', 'true story', 'Islamic'],
        chapters=chapters,
        is_published=True,
        is_completed=True,
        views_count=14820,
        likes_count=3241,
        created_at=datetime(2024, 1, 15),
        updated_at=datetime(2024, 3, 10),
    )
    story.save()

    print(f"  ✅ Story created with {len(chapters)} chapters!")
    print()
    print("=" * 50)
    print("  SuperHub seeded successfully!")
    print(f"  Author login: {AUTHOR_EMAIL}")
    print(f"  Password:     {AUTHOR_PASSWORD}")
    print("=" * 50)


if __name__ == '__main__':
    seed()
