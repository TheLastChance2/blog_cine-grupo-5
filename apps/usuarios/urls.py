from django.urls import path, include
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name= 'registro'),    
]