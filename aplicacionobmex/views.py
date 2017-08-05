from django.shortcuts import render
from aplicacionobmex.forms import InstitucionForm, DireccionForm, ContactForm, CourseForm, OrderForm, TelefonoForm
from aplicacionobmex.models import Institucion, Telefono,Pedido, Contacto, Curso, Inventario, Direccion, Comentario
# Create your views here.

def index(request):
	return render(request, 'index.html')

def institucionForm(request):
	formdire = DireccionForm
	formtel = TelefonoForm
	forminst = InstitucionForm(request.POST or None)
	if forminst.is_valid():
		data = {
			'nombre' : forminst.cleaned_data['nombre'],
			'email' : forminst.cleaned_data['email'],
			'rfc' : forminst.cleaned_data['rfc'],
		}
		forminst.save()
		forminst=InstitucionForm()
		return render(request, 'institucionform.html', {'forminst': forminst, 'data':data})

	return render(request,'institucionform.html',{'forminst':forminst, 'formdire':formdire, 'formtel':formtel})

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
  		formcontact=ContactForm()
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
  		formcourse=CourseForm()
  		return render(request,'contactform.html',{'formcourse':formcourse, 'data':data})
	return render(request,'courseform.html',{'formcourse':formcourse})

def orderForm(request):
	formorder = OrderForm
	return render(request,'orderform.html',{'formorder':formorder})

def contactPage(request):
	contactos = Contacto.objects.all().order_by("nombre")
	return render(request,'contact.html',{'contactos':contactos})

def institutionPage(request):
	return render(request,'institution.html')

def orderPage(request):
	return render(request,'order.html')

def coursePage(request):
	return render(request, 'course.html')
