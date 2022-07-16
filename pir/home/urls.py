from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('home', views.home),
    path('about', views.aboutus, name='aboutus'),
    path('contact', views.contactus, name='contactus'),
    path('services/medical-Billing', views.medical, name='medical'),
    path('services/dental-Billing', views.dental ,name='dental'),
    path('services/credentialing', views.credential, name='credentialing'),
    path('contact_submit',views.contact_submit, name='contact_submit'),
    path('medical_contact_submit',views.medical_submit, name='medical_contact_submit'),
    path('dental_contact_submit',views.dental_submit, name='dental_contact_submit'),
    path('credential_contact_submit',views.credentialing_submit, name='credential_contact_submit'),
    
]