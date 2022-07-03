
from django.urls import path
from .views import segunda_vista, una_vista

urlpatterns = [
    path('',una_vista, name='Home' ),
    path('segundavista',segunda_vista, name='Datos'),
]