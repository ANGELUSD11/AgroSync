from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import handler404

handler404 = 'users.views.error_404_view'


urlpatterns = [
    path('clima/', views.clima_actual, name='clima'),
    path('registrar-cultivo/', views.registrar_cultivo, name='registrar_cultivo'),
    path('lista-cultivos/', views.lista_cultivos, name='lista_cultivos'),  # Nueva ruta
    path('eliminar-cultivo/<int:cultivo_id>/', views.eliminar_cultivo, name='eliminar_cultivo'),
]