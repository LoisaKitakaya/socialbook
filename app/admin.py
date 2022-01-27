from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'first_name', 'second_name', 'joined_on')
    list_filter = ('user', 'joined_on')
    search_fields = ['user', 'first_name', 'second_name']

admin.site.register(UserProfile, UserProfileAdmin)

class PostsAdmin(admin.ModelAdmin):

    list_display = ('post_author', 'title', 'posted_on')
    list_filter = ('post_author', 'posted_on')
    search_fields = ['post_author', 'title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Posts, PostsAdmin)

class CommentsAdmin(admin.ModelAdmin):

    list_display = ('comment_author', 'comment_post', 'commented_on')
    list_filter = ('comment_author', 'comment_post', 'commented_on')
    search_fields = ['comment_author', 'comment_post', 'comment']

admin.site.register(Comments, CommentsAdmin)