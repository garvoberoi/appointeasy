from django.db import models
from datetime import datetime
from phone_field import PhoneField
# Create your models here.

doc_cat = (
    ("genral-physician","General Physician"),
    ("cardiologist", "Cardiologist"),
    ("dramatologist", "Dramatologist"),        
    ("neurologist", "Neurologist"),
    ("physciotherpist","Physciotherpist"),
    ("dentist","Dentist")
)
class Doctor(models.Model):
    docid = models.IntegerField(null=True, default=1001)
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    add = models.TextField()
    email = models.EmailField()
    category = models.CharField(choices=doc_cat,max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Appoint(models.Model):
    f_name = models.CharField(max_length=12)
    l_name = models.CharField(max_length=12)
    phone1 = models.BigIntegerField()
    phone2 = models.BigIntegerField(blank=True, null=True)
    add = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    doctor = models.ForeignKey(Doctor,null=True, blank=True, on_delete=models.CASCADE)
    day = models.CharField(max_length=30)
    timeslot = models.CharField(max_length=30)
    symptom = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.f_name + self.l_name
    
class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    mess = models.TextField()
    email = models.EmailField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


