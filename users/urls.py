from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = 'users.views.error_404_view'

urlpatterns = [
    path('registro/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('mainpage/', views.mainpage, name='mainpage')
]