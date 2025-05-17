from django.shortcuts import render

import os

# Create your views here.
def clima_actual(request):
    ciudad = "Bogotá"
    api_key = os.getenv("WEATHER_KEY")
    lat = 33.44
    lon = -94.04
    api_call = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={api_key}"

    clima_data = {}

    try:
        respuesta = request.get(api_call)
        datos = respuesta.json()

        if respuesta.status_code == 200:

            current = datos['current']

            clima_data = {
            'ciudad': ciudad,
            'temperatura': current['temp'],
            'descripcion': current['weather'][0]['description'].capitalize(),
            'humedad': current['humidity'],
            'viento': current['wind_speed'],
            'sensacion_termica': current['feels_like'],
            'icono': current['weather'][0]['icon']  # opcional para mostrar icono
            }
        else:
            clima_data['error'] = "Error al obtener los datos"

    except Exception as e:
        clima_data['error'] = f"Error al consumir la api: {e}"

    return render(request, 'cultivos/clima.html', {'clima': clima_data})