from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('posts/<slug:slug>/', user_posts, name='posts'),
    path('user/<int:pk>/', user_profile, name='user'),
    path('create_post/', create_post, name='create_post'),
    path('create_new_profile/', create_new_profile, name='create_new_profile'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('liveuser/', current_user_profile, name='liveuser'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)