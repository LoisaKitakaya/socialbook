from django.shortcuts import render, redirect
import requests
import os
from newsapi import NewsApiClient
from .models import *
from .forms import *
import yagmail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login

# Create your views here.

# home view
def home(request):

    # get user currently logged in
    live_user = request.user

    # get user location using ip api
    user_location = requests.get('https://ipapi.co/json/')

    city = user_location.json()['city']

    # get user location weather based on user location
    URL = 'https://api.weatherapi.com/v1/current.json'

    api_key_weather = os.getenv('api_key_weather')

    api_call_query = city

    PARAMS = {
        'key' : api_key_weather,
        'q' : api_call_query
    }

    user_location_weather = requests.get(url = URL, params = PARAMS)

    # show tech news on home page
    # Init
    newsapi = NewsApiClient(api_key=os.getenv('api_key_news'))

    # /v2/top-headlines
    news_feed = newsapi.get_everything(q='tech', sources='the-verge,bbc-news,ars-technica,bloomberg,business-insider', language='en', sort_by='relevancy')

    # get all posts
    all_posts = Posts.objects.select_related('post_author').all()

    comment_count = {}

    for post in all_posts:

        comment_count[post] = Comments.objects.filter(comment_post=post).count()

    # login user
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            return redirect('home')

    else:

        form = AuthenticationForm()

    context = {
        'forecast' : user_location_weather.json(),
        'news_feed' : news_feed['articles'],
        'live_user' : live_user,
        'all_posts' : all_posts,
        'comment_count' : comment_count,
        'form' : form,
    }

    return render(request, 'app/index.html', context)

# posts view
@login_required(login_url='login_user')
def user_posts(request, slug):

    blog_article = Posts.objects.get(slug=slug)

    comment_post = Comments.objects.select_related('comment_author').filter(comment_post=blog_article)

    current_user = request.user

    save_action_user = UserProfile.objects.select_related('user').get(user_id=current_user.pk)

    if request.method == 'POST':

        form = CreateComment(request.POST, request.FILES)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.comment_author = save_action_user

            save_action.comment_post = blog_article

            save_action.save()
            
        return redirect('home')

    else:
        form = CreateComment()

    context = {
        'article' : blog_article,
        'post_comments' : comment_post,
        'form' : form,
    }

    return render(request, 'app/posts.html', context)

# users view
@login_required(login_url='login_user')
def user_profile(request, pk):

    profile = UserProfile.objects.select_related('user').get(user_id=pk)

    posts_profile = Posts.objects.filter(post_author=profile)

    context = {
        'profile' : profile,
        'posts_by_user' : posts_profile,
    }

    return render(request, 'app/user.html', context)

# current user's profile
@login_required(login_url='login_user')
def current_user_profile(request):

    current_user = request.user

    profile = UserProfile.objects.select_related('user').get(user_id=current_user.pk)

    posts_profile = Posts.objects.filter(post_author=profile)

    context = {
        'profile' : profile,
        'posts_by_user' : posts_profile,
    }

    return render(request, 'app/user.html', context)

# create post view
@login_required(login_url='login_user')
def create_post(request):

    current_user = request.user

    save_action_user = UserProfile.objects.select_related('user').get(user_id=current_user.pk)

    if request.method == 'POST':

        form = CreatePost(request.POST, request.FILES)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.post_author = save_action_user

            save_action.save()
            
        return redirect('home')

    else:
        form = CreatePost()

    context = {
        'form' : form,
    }

    return render(request, 'app/create.html', context)

# create new profile view
@login_required(login_url='login_user')
def create_new_profile(request):

    current_user = request.user

    if request.method == 'POST':

        form = CreateProfile(request.POST, request.FILES)

        if form.is_valid():

            save_action = form.save(commit=False)

            save_action.user = current_user

            save_action.save()
            
        return redirect('home')

    else:
        form = CreateProfile()

    context = {
        'form' : form,
    }

    return render(request, 'app/profile.html', context)

# about view
def about(request):

    return render(request, 'app/about.html')

# contact view
def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get('email')

            subject_ = form.cleaned_data.get('subject')

            comment = form.cleaned_data.get('comment')

            message = 'We will get back to you within the hour.'

            yag = yagmail.SMTP('loisadevmode@gmail.com', '#Kitloisa15')

            yag.send(
                to = email,
                subject = subject_,
                contents = message
            )

            yag.send(
                to = 'kitakayaloisa@gmail.com',
                subject =subject_,
                contents = comment
            )
            
        return redirect('home')

    else:
        form = ContactForm()

    context = {
        'form' : form,
    }

    return render(request, 'app/contact.html', context)
