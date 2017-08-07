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
url(r'^contact/(?P<contactID>\d+)/$', views.contactPage, name= 'contactpage'),
url(r'^institution/(?P<institutionID>\d+)/$', views.institutionPage, name= 'institutionpage'),
url(r'^order/(?P<orderID>\d+)/$',views.orderPage, name = 'orderpage'),
url(r'^course/(?P<courseID>\d+)/$',views.coursePage, name = 'coursepage'),
]
