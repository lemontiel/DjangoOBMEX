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
	formdire = DireccionForm
	formcontact = ContactForm(request.POST or None)
	if formcontact.is_valid():
  		data = {
  		'nombre' : formcontact.cleaned_data['nombre'],
  		'apellidoP':formcontact.cleaned_data['apellidoP'],
  		'apellidoM':formcontact.cleaned_data['apellidoM'],
  		'email' : formcontact.cleaned_data['email'],
  		}
  		formcontact.save()
  		return render(request,'contactform.html',{'formcontact':formcontact, 'data':data})
  		return render(request,'contactform.html',{'formcontact':formcontact, 'formcontact':formcontact})


def courseForm(request):
	formdire = DireccionForm
	formcourse = CourseForm(request.POST or None)
	if formcourse.is_valid():
  		data = {
  		'fecha' : formcourse.cleaned_data['fecha'],
  		'hora':formcourse.cleaned_data['hora'],
  		'costo':formcourse.cleaned_data['costo'],
  		}
  		formcourse.save()
  		return render(request,'contactform.html',{'formcourse':formcourse, 'data':data})
	return render(request,'courseform.html',{'formcourse':formcourse})

def orderForm(request):
	formorder = OrderForm
	return render(request,'orderform.html',{'formorder':formorder})
