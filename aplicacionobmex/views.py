from django.shortcuts import render
from aplicacionobmex.forms import InstitucionForm, DireccionForm
from aplicacionobmex.models import Telefono
# Create your views here.

def base(request):
	return render(request, 'base.html')

def institucionForm(request):
	form = InstitucionForm
	formdire = DireccionForm
	telefono = Telefono.objects.all()
	return render(request,'institucionform.html',{'form':form, 'telefono':telefono})
