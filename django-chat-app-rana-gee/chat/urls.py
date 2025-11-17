from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('room/', views.room, name='room'),
    path('post_message/', views.post_message, name='post_message'),
]

# Add this line to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
