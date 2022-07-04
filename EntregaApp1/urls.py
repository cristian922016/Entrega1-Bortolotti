
from django.urls import path
from .views import Datos_usuario, segunda_vista, una_vista

urlpatterns = [
    path('',una_vista, name='Home' ),
    path('segundavista',segunda_vista, name='Datos'),
    path('datos-usuario/',Datos_usuario, name='datos_usuario'),
]