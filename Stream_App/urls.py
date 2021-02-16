from django.contrib import admin
from django.urls import path
from Stream_App import views


app_name = 'Stream_App'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-video/', views.upload_videos, name='upload_videos'),
    path('edit-video/', views.edit_videos, name='edit_videos'),
    path('details-video/<slug:slug>/',
         views.details_videos, name='details_videos'),
    path('my-videos/', views.MyVideos.as_view(), name='my_videos'),
]
