# apps/users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia 'login' por la vista que uses
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
from django.shortcuts import render

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('mainpage')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'users/login.html')

@login_required
def home(request):
    return render(request, 'users/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def mainpage(requets):
    return render(requets, 'users/mainpage.html')
