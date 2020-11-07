from django.shortcuts import render, redirect
from home.models import Appoint, Contact, Doctor
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import Contactform, Appointform
from django.core.mail import send_mail

# username-garv pass-garvob5

def homes(request):
    return render(request, 'index.html', {'name': 'Garv'})

def services(request):
    return render(request, 'services.html', {'name': 'Garv'})

def takeappointment(request, docid):
    doctor = Doctor.objects.get(docid = docid)
    if request.method == 'POST':
        form = Appointform(request.POST, from_doctor=doctor)
        if form.is_valid():
            form.save()
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            day = request.POST['day'] 
            timeslot = request.POST['timeslot']
            email = request.POST['email']
            doctorname = str(form.from_doctor)
            #sending email
            send_mail(
                'Requested Appointment', #subject
                'You requested for an appointment with ' + doctorname + ' on ' + day + ' at ' + timeslot + '. Thankyou ', #message
                'garvoberoi1999@gmail.com', #from email
                [email], #to email
            )
            return render(request, 'submit.html', {
                'f_name' : f_name,
                'l_name' : l_name,
                'day' : day,
                'timeslot' : timeslot,
                'email' : email,
                'doctorname' : doctorname,
                })   
    form = Appointform(from_doctor=doctor)
    return render(request, 'takeappointment.html', {'form': form, 'doctor': doctor})

def contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
    form = Contactform()
    return render(request, 'contact.html', {'form': form})

def Doctorview(request):
    context = Doctor.objects.all()
    if request.method == 'POST':
        cat = request.POST['doctor']
        if cat == 'all':
            context = Doctor.objects.all() 
            return render(request, 'doctor.html', {'context': context}) 
        context = Doctor.objects.all().filter(category=cat)
        return render(request, 'doctor.html', {'context': context})
    return render(request, 'doctor.html', {'context': context}) 

