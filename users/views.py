# apps/users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages
import requests  # Asegúrate de importar requests

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


def mainpage(request):
    ciudad = "Tunja"
    api_key = "4b6556d8c3f5006f717e2e9b74ec0edb"
    api_call = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad},co&APPID={api_key}'
    clima_data = {}

    try:
        respuesta = requests.get(api_call)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            clima_data = {
                'ciudad': ciudad,
                'temperatura': round(datos['main']['temp']-273.15),
                'descripcion': datos['weather'][0]['description'].capitalize(),
                'humedad': datos['main']['humidity'],
                'viento': datos['wind']['speed'],
                'icono': datos['weather'][0]['icon']
            }
        else:
            clima_data['error'] = f"Error al obtener los datos: {respuesta.status_code} - {respuesta.json().get('message')}"
    except Exception as e:
        clima_data['error'] = f"Error al consumir la API: {e}"

    return render(request, 'users/mainpage.html', {'clima': clima_data})