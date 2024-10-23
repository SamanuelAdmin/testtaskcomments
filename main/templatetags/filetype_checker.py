from django import template
import mimetypes

register = template.Library()

@register.filter(name="fileMime")
def fileMime(value):
    return mimetypes.guess_type(value)[0]