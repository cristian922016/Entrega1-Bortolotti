
from django.urls import path
from .views import Datos_usuario, segunda_vista, una_vista,primera_vista

urlpatterns = [
    path('',primera_vista, name='Home' ),
    path('una-vista',una_vista, name='agregar'),
    path('segundavista',segunda_vista, name='Datos'),
    path('datos-usuario/',Datos_usuario, name='datos_usuario'),
]