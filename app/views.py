from django.shortcuts import render, redirect

# Create your views here.
def home(request):

    return render(request, 'app/index.html')

def user_posts(request):

    return render(request, 'app/posts.html')

def user_profile(request):

    return render(request, 'app/user.html')

def about(request):

    return render(request, 'app/about.html')

def contact(request):

    return render(request, 'app/contact.html')
