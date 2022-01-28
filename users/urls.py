from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('login_user/', login_user, name='login_user'),
    path('login_new_user/', login_new_user, name='login_new_user'),
    path('logout_user/', logout_user, name='logout_user'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)