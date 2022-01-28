# forms code go here
from cProfile import label
from django import forms
from .models import *
from cloudinary.forms import CloudinaryFileField 

# create form post
class CreatePost(forms.ModelForm):

    class Meta:

        model = Posts

        fields = '__all__'
        exclude = ['post_author', 'slug', 'posted_on']
        post_thumbnail = CloudinaryFileField('image')

# create profile form
class CreateProfile(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = '__all__'
        exclude = ['user', 'joined_on']
        profile_pic = CloudinaryFileField('image')

# create comment form
class CreateComment(forms.ModelForm):

    class Meta:

        model = Comments

        fields = '__all__'
        exclude = ['comment_author', 'comment_post', 'commented_on']

# contact form
class ContactForm(forms.Form):

    email = forms.EmailField(label='Your email')
    subject = forms.CharField(label='Subject', max_length=100)
    comment = forms.CharField(label='Talk to us...', widget=forms.Textarea)