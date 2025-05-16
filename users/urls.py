from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = 'users.views.error_404_view'

urlpatterns = [
    path('registro/', views.register, name='register'),
]