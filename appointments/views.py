from django.shortcuts import render
from django.http import HttpResponseRedirect
from appointments.models import Appointment
from .forms import AppointmentForm

def showAppointments(request):
    appts = Appointment.objects.all()
    return render(request, 'appointments/display.html', {'appts' : appts})
    

def createAppointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            patient_name = form.cleaned_data['patient_name']
            doc_name = form.cleaned_data['doc_name']
            appt_date = form.cleaned_data['appt_date']
            appt_time = form.cleaned_data['appt_time']

            Appointment.objects.create (
                patient_name = patient_name,
                doc_name = doc_name,
                appt_date = appt_date,
                appt_time = appt_time,
            ).save()

            return HttpResponseRedirect('/appointments')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/create.html', {'form' : form})


def home(request):
    return render(request, 'appointments/home.html')

