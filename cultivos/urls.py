from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import handler404

handler404 = 'users.views.error_404_view'


urlpatterns = [
    path('clima/', views.clima_actual, name='clima')
]