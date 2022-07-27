
from django.urls import path
from .views import Datos_usuario, segunda_vista, una_vista,primera_vista,Eliminar_dato,Editar_dato,Mostrar_dato

urlpatterns = [
    path('',primera_vista, name='Home' ),
    path('una-vista',una_vista, name='agregar'),
    path('segundavista',segunda_vista, name='Datos'),
    path('datos-usuario/',Datos_usuario, name='datos_usuario'),
    path('eliminar-dato/<int:id>',Eliminar_dato, name='eliminar'),
    path('editar-dato/<int:id>',Editar_dato, name='editar'),
    path('mostrar-dato/<int:id>',Mostrar_dato, name='Mostrar'),
]