from django.shortcuts import render
from aplicacionobmex.forms import InstitucionForm, DireccionForm, ContactForm, CourseForm, OrderForm
from aplicacionobmex.models import Telefono
# Create your views here.

def base(request):
	return render(request, 'base.html')

def institucionForm(request):
	formdire = DireccionForm
	forminst = InstitucionForm(request.POST or None)
	if forminst.is_valid():
		data = {
			'nombre' : forminst.cleaned_data['nombre'],
			'email' : forminst.cleaned_data['email'],
			'rfc' : forminst.cleaned_data['rfc'],
		}
		forminst.save()
		return render(request, 'institucionform.html', {'forminst': forminst, 'data':data})

	return render(request,'institucionform.html',{'forminst':forminst, 'formdire':formdire})

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
