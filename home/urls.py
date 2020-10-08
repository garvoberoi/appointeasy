from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.homes, name='homes'),
    path('services', views.services, name='services'),
    path('takeappointment/<int:docid>', views.takeappointment, name='takeappointment'),
    path('contact', views.contact, name='contact'),
    path('doctor', views.Doctorview, name='doctor'),
]
