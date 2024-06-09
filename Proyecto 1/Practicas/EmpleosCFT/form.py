from django.forms import ModelForm 
from .models import crear_vacante

class formvacante(ModelForm):
    class Meta:
        model = crear_vacante
        fields =['titulo','carrera','modalidad','descripcion','ubicacion']
    