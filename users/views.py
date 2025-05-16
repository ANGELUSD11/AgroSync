# apps/users/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia 'login' por la vista que uses
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
