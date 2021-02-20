from django.contrib import admin
from django.urls import path
from Stream_App import views


app_name = 'Stream_App'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-video/', views.upload_videos, name='upload_videos'),
    path('add-category/', views.add_category.as_view(), name='add_category'),
    path('edit-video/<slug:slug>/', views.edit_video, name='edit_video'),
    path('details-video/<slug:slug>/',
         views.details_videos, name='details_videos'),
    path('my-videos/', views.MyVideos.as_view(), name='my_videos'),
    path('delete-video/<pk>/', views.Delete_Video.as_view(), name='delete_video'),
    path('categories/', views.categories, name='categories'),
]
