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


@register.filter
def compact_number(value):
    """Format large numbers: 1000 → 1K, 100000 → 100K, 1000000 → 1M"""
    try:
        n = int(value)
    except (ValueError, TypeError):
        return value
    if n >= 1_000_000:
        result = n / 1_000_000
        return f'{result:.1f}M'.rstrip('0').rstrip('.') + 'M' if result != int(result) else f'{int(result)}M'
    if n >= 1_000:
        result = n / 1_000
        return f'{result:.1f}K'.rstrip('0').rstrip('.') + 'K' if result != int(result) else f'{int(result)}K'
    return str(n)
