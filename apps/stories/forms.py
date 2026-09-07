from django import forms
from .models import GENRES


class StoryForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Story title',
            'class': 'form-input'
        })
    )
    description = forms.CharField(
        required=False,
        max_length=1000,
        widget=forms.Textarea(attrs={
            'placeholder': 'What is your story about?',
            'class': 'form-input',
            'rows': 4
        })
    )
    genre = forms.ChoiceField(
        choices=[(g, g) for g in GENRES],
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    tags = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tags separated by commas  e.g. love, faith, Nigeria',
            'class': 'form-input'
        })
    )
    cover_image = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'placeholder': 'Cover image URL (optional)',
            'class': 'form-input'
        })
    )
    is_published = forms.BooleanField(
        required=False,
        label='Publish immediately (readers can see it)'
    )
    is_completed = forms.BooleanField(
        required=False,
        label='Mark as completed'
    )


class ChapterForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Chapter title',
            'class': 'form-input'
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your chapter here...',
            'class': 'form-input',
            'rows': 25,
            'style': 'font-family: Georgia, serif; font-size: 1rem; line-height: 1.8;'
        })
    )
