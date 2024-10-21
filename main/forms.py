from django import forms
from .models import *

# captcha
from django.conf import settings
from captcha.fields import CaptchaField



class AddCommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['username', 'email', 'homepage', 'text']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'homepage': forms.URLInput(attrs={'placeholder': 'Homepage'}),
            'text': forms.Textarea(attrs={'class': 'text-input', 'placeholder': 'Enter your comment'}),
        }
        labels = {
            'homepage': 'Your home page URL',
            'text': 'Your comment'
        }