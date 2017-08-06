# aplicacionobmex/urls.py
from django.conf.urls import url
from aplicacionobmex import views

urlpatterns = [
url(r'^$', views.index.as_view(), name='index'),
url(r'^institucionform/$', views.institucionForm, name= 'institucionform'),
url(r'^contactform/$', views.contactForm, name= 'contactform'),
url(r'^courseform/$', views.courseForm, name= 'courseform'),
url(r'^orderform/$', views.orderForm, name= 'orderform'),
url(r'^inventoryform/$', views.inventoryForm, name= 'inventoryform'),
url(r'^contact/(?P<contactID>[0,9]{7})/$', views.contactPage, name= 'contactpage'),
url(r'^institution/(?P<institutionID>[0,9]{7})/$', views.institutionPage, name= 'institutionpage'),
url(r'^order/(?P<orderID>[0,9]{7})/$',views.orderPage, name = 'orderpage'),
url(r'^course/(?P<courseID>[0,9]{7})/$',views.coursePage, name = 'coursepage'),
]