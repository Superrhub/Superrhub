from mongoengine import (
    Document, StringField, ListField,
    DateTimeField, BooleanField, EmailField
)
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password as django_check_password


class User(Document):
    username = StringField(required=True, unique=True, max_length=50)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    bio = StringField(max_length=500, default='')
    avatar = StringField(default='')
    followers = ListField(StringField())
    following = ListField(StringField())
    created_at = DateTimeField(default=datetime.utcnow)
    is_active = BooleanField(default=True)

    meta = {'collection': 'users'}

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return django_check_password(raw_password, self.password)

    @property
    def followers_count(self):
        return len(self.followers)

    @property
    def following_count(self):
        return len(self.following)

    def __str__(self):
        return self.username
