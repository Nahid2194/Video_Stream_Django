from django import forms
from .models import Comment, Video, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['category', 'video_title', 'video_content', 'thumbnail']
