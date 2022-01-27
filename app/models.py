from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from slugger import AutoSlugField

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users', primary_key=True, blank=True)
    first_name = models.CharField(max_length=50, unique=True)
    second_name = models.CharField(max_length=50, unique=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField()
    joined_on = models.DateField(auto_now_add=True)

    class Meta:

        ordering = ['-joined_on']

    def __str__(self):

        return self.first_name

class Posts(models.Model):

    post_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_profiles', blank=True)
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title')
    post_thumbnail = CloudinaryField('image')
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-posted_on']

    def __str__(self):

        return self.title

class Comments(models.Model):

    comment_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True,related_name='commenting_user')
    comment_post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True,related_name='commented_post')
    comment = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-commented_on']

    def __str__(self):

        return self.comment
