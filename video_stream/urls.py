from django.contrib import admin
from django.urls import path, include

# To show media files
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from Stream_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login_App.urls')),
    path('stream/', include('Stream_App.urls')),
    path('', views.home, name='home'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
