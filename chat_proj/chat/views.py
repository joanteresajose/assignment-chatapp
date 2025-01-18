

from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'chat/login.html')  # Redirect to login if not authenticated
    
    users = User.objects.exclude(username=request.user.username)  # Exclude the logged-in user
    return render(request, 'chat/home.html', {'users': users})

from django.contrib.auth.decorators import login_required

@login_required
def chat_view(request):
    return render(request, 'chat/chat.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('home')  # Redirect to the home page after sign-up
    else:
        form = UserCreationForm()
    
    return render(request, 'chat/signup.html', {'form': form})

from django.shortcuts import redirect
from django.contrib.auth import logout

def custom_logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page
