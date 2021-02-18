from django import forms
from .models import Comment, Video


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['video_title', 'video_content', 'thumbnail']
