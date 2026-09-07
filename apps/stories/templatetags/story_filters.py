from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def split_paragraphs(value):
    """Split text into paragraphs by blank lines."""
    if not value:
        return []
    paragraphs = re.split(r'\n\s*\n', value.strip())
    return [p.strip() for p in paragraphs if p.strip()]


@register.filter
def linebreak_tag(value):
    """Convert double newlines to <p> tags for reader display."""
    if not value:
        return mark_safe('')
    paragraphs = re.split(r'\n\s*\n', value.strip())
    html = ''.join(
        f'<p>{p.strip().replace(chr(10), "<br />")}</p>'
        for p in paragraphs if p.strip()
    )
    return mark_safe(html)
