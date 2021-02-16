from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import CommentForm, VideoForm
import uuid
from .models import Comment, Video
# Create your views here.


def home(request):
    return render(request, 'Stream_App/home.html', context={})


def upload_videos(request):
    return render(request, 'Stream_App/home.html')


def edit_videos(request):
    return render(request, 'Stream_App/home.html')


def details_videos(request):
    return render(request, 'Stream_App/home.html')
