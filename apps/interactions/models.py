from mongoengine import Document, StringField, DateTimeField, BooleanField, FloatField, IntField
from datetime import datetime


class Like(Document):
    user_id = StringField(required=True)
    story_id = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'likes', 'indexes': [('user_id', 'story_id')]}


class Comment(Document):
    user_id = StringField(required=True)
    username = StringField(required=True)
    story_id = StringField(required=True)
    content = StringField(required=True, max_length=500)
    created_at = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'comments', 'indexes': ['story_id']}


class ReadingList(Document):
    user_id = StringField(required=True)
    story_id = StringField(required=True)
    story_title = StringField(default='')
    author_username = StringField(default='')
    cover_image = StringField(default='')
    genre = StringField(default='')
    added_at = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'reading_lists', 'indexes': ['user_id']}


class Purchase(Document):
    user_id = StringField(required=True)
    story_id = StringField(required=True)
    amount = FloatField(required=True)
    reference = StringField(required=True)
    verified = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
    meta = {
        'collection': 'purchases',
        'indexes': [('user_id', 'story_id'), 'reference'],
    }


class Notification(Document):
    """In-app notifications for story authors."""
    recipient_id = StringField(required=True)   # story author
    sender_username = StringField(required=True) # who triggered it
    notif_type = StringField(required=True)      # 'like', 'comment', 'follow'
    story_id = StringField(default='')
    story_title = StringField(default='')
    message = StringField(required=True)
    is_read = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'notifications',
        'indexes': ['recipient_id', 'is_read'],
    }


class ReadingProgress(Document):
    """Tracks which chapter a user left off on."""
    user_id = StringField(required=True)
    story_id = StringField(required=True)
    story_title = StringField(default='')
    cover_image = StringField(default='')
    author_username = StringField(default='')
    last_chapter = IntField(default=1)
    last_chapter_title = StringField(default='')
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'reading_progress',
        'indexes': ['user_id', ('user_id', 'story_id')],
    }
