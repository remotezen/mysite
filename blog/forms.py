from django import forms
from .models import Post, Comment


"""
As you might've guessed PostForm is the name of
our form
"""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
