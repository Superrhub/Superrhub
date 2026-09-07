from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class Like(Document):
    user_id = StringField(required=True)
    story_id = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'likes',
        'indexes': [('user_id', 'story_id')],
    }


class Comment(Document):
    user_id = StringField(required=True)
    username = StringField(required=True)
    story_id = StringField(required=True)
    content = StringField(required=True, max_length=500)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'comments',
        'indexes': ['story_id'],
    }


class ReadingList(Document):
    user_id = StringField(required=True)
    story_id = StringField(required=True)
    story_title = StringField(default='')
    author_username = StringField(default='')
    cover_image = StringField(default='')
    genre = StringField(default='')
    added_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'reading_lists',
        'indexes': ['user_id'],
    }
