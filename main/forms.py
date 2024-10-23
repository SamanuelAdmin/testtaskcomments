from random import random

from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import *
from .modules import permitted_html_elements
from .modules import queue
from .modules import html_tag_parser

# captcha
from captcha.fields import CaptchaField

import random as rand




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


@deconstructible
class FileValidator:
    code = 'filevalidator'

    def __init__(self, incorrectTypeError=None, tooLargeFileError=None):
        self.incorrectTypeError = incorrectTypeError if incorrectTypeError else "Incorrect file type"
        self.tooLargeFileError = tooLargeFileError if tooLargeFileError else "Too large file"

        self.validMimeType = ['image/jpeg', 'image/png', 'image/gif', 'image/jpg', 'text/plain']
        self.checkSizeFileTypes = ['text/plain'] # types of files where we need to chech a size
        self.validFileSize = 100 * 1024 # max size for those files

    def __call__(self, file, *args, **kwargs):
        # check file type
        if file.content_type not in self.validMimeType:
            print(file.content_type)
            raise ValidationError(self.incorrectTypeError, code=self.code)

        # check file size (if file is a text document)
        if file.content_type in self.checkSizeFileTypes:
            if file.size > self.validFileSize:
                raise ValidationError(self.tooLargeFileError, code=self.code)




class AddCommentForm(forms.ModelForm):
    captcha = CaptchaField()

    def save(self, commit=True):
        htmlValidator = HtmlValidator()
        fileValidator = FileValidator()

        try:
            htmlValidator(self.cleaned_data.get('text')) # checking for banned HTML tags
        except ValidationError as e:
            self.add_error('text', e)
            return None

        file = self.cleaned_data.get('file')

        if file:
            try: fileValidator(file)
            except ValidationError as e:
                self.add_error('file', e)
                return None

        return super(AddCommentForm, self).save(commit=commit)


    class Meta:
        model = Comment
        fields = ['username', 'email', 'homepage', 'text', 'file']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'homepage': forms.URLInput(attrs={'placeholder': 'Homepage'}),
            'text': forms.Textarea(
                attrs={'class': 'text-input', 'placeholder': 'Enter your comment', 'id': 'commentTextArea'},
            ),
            'file': forms.FileInput(attrs={'class': 'file-input-button', 'placeholder': 'Attached file', 'accept': ".jpg, .jpeg, .gif, .png, .txt"}),
        }

        labels = {
            'homepage': 'Your home page URL',
            'text': 'Your comment'
        }