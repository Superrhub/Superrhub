from mongoengine import (
    Document, EmbeddedDocument, StringField, IntField,
    BooleanField, DateTimeField, ListField, EmbeddedDocumentField
)
from datetime import datetime

GENRES = [
    'Romance', 'Fiction', 'Non-Fiction', 'Poetry',
    'Mystery', 'Thriller', 'Fantasy', 'Biography', 'Self-Help', 'Other'
]


class Chapter(EmbeddedDocument):
    chapter_number = IntField(required=True)
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f'Chapter {self.chapter_number}: {self.title}'


class Story(Document):
    title = StringField(required=True, max_length=200)
    description = StringField(max_length=1000, default='')
    cover_image = StringField(default='')
    author_id = StringField(required=True)
    author_username = StringField(required=True)
    genre = StringField(choices=GENRES, default='Fiction')
    tags = ListField(StringField(max_length=30))
    chapters = ListField(EmbeddedDocumentField(Chapter))
    is_published = BooleanField(default=False)
    is_completed = BooleanField(default=False)
    views_count = IntField(default=0)
    likes_count = IntField(default=0)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'stories',
        'indexes': ['author_id', 'genre', 'is_published'],
    }

    @property
    def chapters_count(self):
        return len(self.chapters)

    @property
    def cover_color(self):
        """Return a gradient color based on genre for placeholder covers."""
        colors = {
            'Romance': 'from-rose-900 to-pink-800',
            'Fiction': 'from-blue-900 to-indigo-800',
            'Non-Fiction': 'from-gray-800 to-gray-700',
            'Poetry': 'from-purple-900 to-violet-800',
            'Mystery': 'from-gray-900 to-zinc-800',
            'Thriller': 'from-red-900 to-orange-900',
            'Fantasy': 'from-emerald-900 to-teal-800',
            'Biography': 'from-amber-900 to-yellow-800',
            'Self-Help': 'from-cyan-900 to-sky-800',
            'Other': 'from-orange-900 to-amber-800',
        }
        return colors.get(self.genre, 'from-orange-900 to-amber-800')

    def __str__(self):
        return self.title
