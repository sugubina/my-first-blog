from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'photo')

class DeleteForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = []




