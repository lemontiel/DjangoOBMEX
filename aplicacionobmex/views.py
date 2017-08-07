from django.shortcuts import render
from django.views.generic import TemplateView
from aplicacionobmex.forms import InstitucionForm, DireccionForm, InventoryForm, ContactForm, CourseForm, OrderForm, TelefonoForm
from aplicacionobmex.models import Institucion, Telefono,Pedido, Contacto, Curso, Inventario, Direccion, Comentario
# Create your views here.

class index(TemplateView):
	template_name = "index.html"

def institucionForm(request):
	formdire = DireccionForm
	formtel = TelefonoForm
	forminst = InstitucionForm(request.POST or None)
	if forminst.is_valid():
		forminst.save()
		forminst=InstitucionForm()
	institution=Institucion.objects.all()
	return render(request,'institucionform.html',{'forminst':forminst, 'formdire':formdire, 'institution':institution, 'formtel':formtel})

def contactForm(request):
	formdire = DireccionForm
	formcontact = ContactForm(request.POST or None)
	if formcontact.is_valid():
  		formcontact.save()
  		formcontact=ContactForm()
	contact=Contacto.objects.all()
	return render(request,'contactform.html',{'formcontact':formcontact, 'contact':contact})

def inventoryForm(request):
	forminventory = InventoryForm(request.POST or None)
	if forminventory.is_valid():
		forminventory.save()
		forminventory=InventoryForm()
	inventory=Inventario.objects.all()
	return render(request,'inventoryform.html',{'forminventory':forminventory, 'inventory':inventory})

def courseForm(request):
	formdire = DireccionForm
	formcourse = CourseForm(request.POST or None)
	if formcourse.is_valid():
  		formcourse.save()
  		formcourse=CourseForm()
	course=Curso.objects.all()
	return render(request,'courseform.html',{'formcourse':formcourse, 'course':course})

def orderForm(request):
	formorder = OrderForm
	return render(request,'orderform.html',{'formorder':formorder})

def contactPage(request, contactID):
	contacto = Contacto.objects.get(id_Contacto = contactID)
	return render(request,'contact.html',{'contacto' : contacto})

def institutionPage(request):
	return render(request,'institution.html')

def orderPage(request):
	return render(request,'order.html')

def coursePage(request):
	return render(request, 'course.html')
