from django.db import models
from django.contrib.auth.models import User

class crear_vacante(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    carrera = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.empresa, self.titulo, self.carrera
        