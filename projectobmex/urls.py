"""projectobmex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from aplicacionobmex import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^institucionform/$', views.institucionForm, name= 'institucionform'),
    url(r'^contactform/$', views.contactForm, name= 'contactform'),
    url(r'^courseform/$', views.courseForm, name= 'courseform'),
    url(r'^orderform/$', views.orderForm, name= 'orderform'),
    url(r'^contact/(?P<contactID>[0,9]{7})/$', views.contactPage, name= 'contactpage'),
    url(r'^institution/(?P<institutionID>[0,9]{7})/$', views.institutionPage, name= 'institutionpage'),
    url(r'^order/(?P<orderID>[0,9]{7})/$',views.orderPage, name = 'orderpage'),
    url(r'^course/(?P<courseID>[0,9]{7})/$',views.coursePage, name = 'coursepage'),
]
