from django.shortcuts import render
from aplicacionobmex.forms import InstitucionForm, DireccionForm, ContactForm, CourseForm, OrderForm
from aplicacionobmex.models import Telefono
# Create your views here.

def base(request):
	return render(request, 'base.html')

def institucionForm(request):
	form = InstitucionForm
	formdire = DireccionForm
	telefono = Telefono.objects.all()
	return render(request,'institucionform.html',{'form':form, 'telefono':telefono})

def contactForm(request):
  form = ContactForm
  formdire = DireccionForm
  telefono = Telefono.objects.all()
  return render(request,'contactform.html',{'form':form, 'telefono':telefono})

def courseForm(request):
  form = CourseForm
  formdire = DireccionForm
  return render(request,'courseform.html',{'form':form})

def orderForm(request):
  form = OrderForm
  return render(request,'orderform.html',{'form':form})