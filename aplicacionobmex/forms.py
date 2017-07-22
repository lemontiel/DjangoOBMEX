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

class ContactForm(ModelForm):
  class Meta:
    model=Contacto
    fields=[ 'nombre', 'apellidoP', 'apellidoM', 'cargo', 'telefono', 'email']

class CourseForm(ModelForm):
  class Meta:
    model=Curso
    fields=[ 'fecha', 'hora', 'costo', 'direccion','instructor']

class OrderForm(ModelForm):
  class Meta:
    model=Pedido
    fields=[ 'tipoSilla', 'monto']