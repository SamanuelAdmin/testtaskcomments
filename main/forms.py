from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import *
from .modules import permitted_html_elements
from .modules import queue
from .modules import html_tag_parser

# captcha
from captcha.fields import CaptchaField





@deconstructible
class HtmlValidator:
    code = 'htmlvalidator'

    def __init__(self, unpermTagError=None, unperrmAttrError=None, notclosedTags=None):
        self.unpermTagError = unpermTagError if unpermTagError else "Unpermitted HTML tags"
        self.unperrmAttrError = unperrmAttrError if unperrmAttrError else "Unpermitted HTML tag attribute"
        self.notclosedTags = notclosedTags if notclosedTags else "Please, close all elements"
        self.htmlTagParser = html_tag_parser.MyHTMLParser(queue.AdvancedQueue)

    def __call__(self, value, *args, **kwargs):
        self.htmlTagParser.feed(value)

        for _ in range(len(self.htmlTagParser.advTagQueue)):
            tagName, tagAttrs = self.htmlTagParser.advTagQueue.get_()

            # check for valid elements
            if tagName not in permitted_html_elements.permittedTags:
                raise ValidationError(self.unpermTagError, code=self.code)

            # check for valid tags
            for attr in tagAttrs:
                if attr[0] not in permitted_html_elements.permittedAttrs:
                    raise ValidationError(self.unperrmAttrError, code=self.code)

        # check if all tags have been closed
        if not self.htmlTagParser.checkOpenTags():
            raise ValidationError(self.notclosedTags, code=self.code)


class AddCommentForm(forms.ModelForm):
    captcha = CaptchaField()

    def save(self):
        validator = HtmlValidator()

        try:
            validator(self.data.get('text')) # checking for banned HTML tags
        except ValidationError as e:
            self.add_error('text', e)
            return None

        super(AddCommentForm, self).save()

    class Meta:
        model = Comment
        fields = ['username', 'email', 'homepage', 'text']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'homepage': forms.URLInput(attrs={'placeholder': 'Homepage'}),
            'text': forms.Textarea(
                attrs={'class': 'text-input', 'placeholder': 'Enter your comment', 'id': 'commentTextArea'},
            ),
        }

        labels = {
            'homepage': 'Your home page URL',
            'text': 'Your comment'
        }