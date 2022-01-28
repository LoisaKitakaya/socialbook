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

# contact form
class ContactForm(forms.Form):

    first_name = forms.CharField(label='Your first name', max_length=50)
    second_name = forms.CharField(label='Your second name', max_length=50)
    email = forms.EmailField(label='Your email')
    subject = forms.CharField(label='Subject', max_length=100)
    comment = forms.CharField(label='Talk to us...', widget=forms.Textarea)