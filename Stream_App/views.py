from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, VideoForm
import uuid
from .models import Comment, Video
# Create your views here.


def home(request):
    videos = Video.objects.all()
    return render(request, 'Stream_App/home.html', context={'videos': videos})


@login_required
def upload_videos(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            title = video.video_title
            video.user = request.user
            video.slug = title.replace(' ', '-') + str(uuid.uuid4())
            video.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Stream_App/upload_videos.html', context={'form': form})


def edit_videos(request):
    return render(request, 'Stream_App/home.html')


def details_videos(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'Stream_App/home.html', context={'video': video})
