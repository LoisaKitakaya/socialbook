from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as django_logout, login as django_login

# Create your views here.

# register user
def register_user(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login_new_user')

        else:

            for msg in form.error_messages:
                    
                print(form.error_messages[msg])

    else:

        form = CustomUserCreationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context)

# login user
def login_user(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            return redirect('home')

    else:

        form = AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/login.html', context)

# login user
def login_new_user(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            return redirect('create_new_profile')

    else:

        form = AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'users/login.html', context)

# logout user
def logout_user(request):

    django_logout(request)

    return redirect('home')