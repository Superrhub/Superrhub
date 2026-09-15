from mongoengine import Document, StringField, DateTimeField, BooleanField, FloatField, IntField
from datetime import datetime, timedelta
import secrets


def _default_expiry():
    return datetime.utcnow() + timedelta(hours=1)


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


class PasswordResetToken(Document):
    """One-time token for password reset. Expires in 1 hour."""
    user_id = StringField(required=True)
    email = StringField(required=True)
    token = StringField(required=True, unique=True)
    expires_at = DateTimeField(default=_default_expiry)
    used = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'password_reset_tokens',
        'indexes': ['token', 'user_id'],
    }

    @classmethod
    def create_for_user(cls, user):
        """Delete any existing tokens for this user and create a fresh one."""
        cls.objects(user_id=str(user.id)).delete()
        token = secrets.token_urlsafe(32)
        return cls(
            user_id=str(user.id),
            email=user.email,
            token=token,
        ).save()

    def is_valid(self):
        return not self.used and datetime.utcnow() < self.expires_at


class CommentReport(Document):
    """A user's report of an inappropriate comment."""
    comment_id    = StringField(required=True)
    comment_text  = StringField(default='')   # snapshot so admin can read it even if deleted
    reported_by   = StringField(required=True)  # username of reporter
    reporter_id   = StringField(required=True)
    reason        = StringField(required=True)  # 'spam', 'hate', 'inappropriate', 'other'
    resolved      = BooleanField(default=False)
    created_at    = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'comment_reports',
        'indexes': ['comment_id', 'resolved'],
    }
