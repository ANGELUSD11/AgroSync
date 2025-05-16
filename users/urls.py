from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.register, name='register'),
    path('mainpage/', views.mainpage, name='mainpage')
]