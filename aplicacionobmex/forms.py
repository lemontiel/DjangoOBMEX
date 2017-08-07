import datetime
import time

from django import forms
from django.forms import ModelForm, Textarea
from aplicacionobmex.models import Institucion, Telefono, Pedido, Contacto, Curso, Inventario, Direccion, Comentario

class InstitucionForm(ModelForm):
  class Meta:
    model=Institucion
    fields=['id_Institucion','nombre','email','rfc','direccion']
    widgets={'id_Institucion': forms.HiddenInput()}

class DireccionForm(ModelForm):
  class Meta:
    model=Direccion
    fields=['estado','calle','numero']

class ContactForm(ModelForm):
  class Meta:
    model=Contacto
    fields=[ 'nombre', 'apellidoP', 'apellidoM', 'cargo','email','institucion']

class InventoryForm(ModelForm):
  class Meta:
    model=Inventario
    fields=['generacion', 'existencias']

class CourseForm(ModelForm):
  class Meta:
    model=Curso
    fields=[ 'fecha', 'hora', 'costo', 'direccion','instructor']

class OrderForm(ModelForm):
  class Meta:
    model=Pedido
    fields=[ 'tipoSilla', 'cantidad', 'monto', 'institucion', 'contacto']

class TelefonoForm(ModelForm):
    class Meta:
        model=Telefono
        fields=['lada', 'tipo', 'numero', 'extencion', 'contacto']

class ComentarioForm(ModelForm):
    class Meta:
        model=Comentario
        fields=['texto']
        widgets = { 'texto': Textarea(attrs={'cols': 55, 'rows': 15}), }