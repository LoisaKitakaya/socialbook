from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('posts/', user_posts, name='posts'),
    path('user/', user_profile, name='user'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)