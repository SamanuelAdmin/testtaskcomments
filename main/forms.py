from django import forms
from .models import *

class AddCommentForm(forms.ModelForm):
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