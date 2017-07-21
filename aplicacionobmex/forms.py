import datetime
import time

from django.forms import ModelForm
from aplicacionobmex.models import Institucion, Telefono, Pedido, Contacto, Curso, Inventario, Direccion, Comentario

class InstitucionForm(ModelForm):
    class Meta:
        model=Institucion
        fields=['nombre','email','rfc','telefono','direccion']
        

class DireccionForm(ModelForm):
    class Meta:
        model=Direccion
        fields=['estado','calle','numero']
