
from django.contrib import admin
from django.urls import path
from Practicas.EmpleosCFT.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('registro/', registro, name = 'registro'),
    path('iniciar_sesion/', IniciarSesion, name = 'login'),
    path('publicaciones/', publicacion, name = 'publicacion'),
    path('crear_publicacion/', crear, name = 'creacion'),
    path('cerrar_sesion/', cerrar_sesion, name = 'salir'),
    path('editar/<int:id_publicacion>', modificar, name = 'editar'),
    path('borrar/<int:id_publicacion>', eliminar, name = 'borrar'),
]
