from django.shortcuts import render, redirect
from .forms import CultivoForm
import os
import requests

def clima_actual(request):
    ciudad = "Bogotá"
    api_key = "4b6556d8c3f5006f717e2e9b74ec0edb"  # o puedes ponerla directo aquí para pruebas

    lat = 4.7110
    lon = -74.0721

    api_call = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=4b6556d8c3f5006f717e2e9b74ec0edb'
    clima_data = {}

    try:
        respuesta = requests.get(api_call)
        if respuesta.status_code == 200:
            datos = respuesta.json()

            clima_data = {
                'ciudad': ciudad,
                'temperatura': datos['main']['temp'],
                'descripcion': datos['weather'][0]['description'].capitalize(),
                'humedad': datos['main']['humidity'],
                'viento': datos['wind']['speed'],
                'sensacion_termica': datos['main']['feels_like'],
                'icono': datos['weather'][0]['icon']
            }
        else:
            clima_data['error'] = f"Error al obtener los datos: {respuesta.status_code} - {respuesta.json().get('message')}"

    except Exception as e:
        clima_data['error'] = f"Error al consumir la API: {e}"

    return render(request, 'cultivos/clima.html', {'clima': clima_data})

def registrar_cultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el cultivo en la base de datos
            return redirect('cultivos')  # Redirige a la lista de cultivos (suponiendo que tienes una vista para ello)
    else:
        form = CultivoForm()

    return render(request, 'registrar_cultivo.html', {'form': form})