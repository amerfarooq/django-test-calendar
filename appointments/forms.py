from django import forms
from .models import Appointment, Doctor
import datetime

class AppointmentForm(forms.ModelForm):
    patient_name = forms.CharField(label = 'Patient Name', max_length=128)
    doc_name = forms.ModelChoiceField(label = 'Select Doctor', queryset=Doctor.objects.all())
    appt_date = forms.DateField(label = 'Appointment Date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    appt_time = forms.TimeField(label = 'Appointment Time')

    def clean(self):
        """ Checks if two appointments overlap by comparing their dates and times """
        cleaned_data = super().clean()
        appt_date = cleaned_data.get("appt_date")
        appt_time = cleaned_data.get("appt_time")
        doc_name = cleaned_data.get("doc_name")
       
        all_appts = Appointment.objects.all()
        
        if appt_date and appt_time and doc_name:
            for appt in all_appts:  
                if appt.appt_date == appt_date and appt.doc_name == doc_name :

                    delta = datetime.timedelta(minutes=30)

                    before_30m = (datetime.datetime.combine(appt.appt_date, appt.appt_time) - delta).time()
                    after_30m = (datetime.datetime.combine(appt.appt_date, appt.appt_time) + delta).time()

                    if (appt_time > before_30m) and (appt_time < after_30m):
                        raise forms.ValidationError("An appointment has already been scheduled for this date and time!")


    def clean_appt_date(self):
        """ Checks if appt_date is not earlier than the current date"""

        form_date = self.cleaned_data['appt_date']

        if form_date < datetime.datetime.now().date():
            raise forms.ValidationError("Appointment must be scheduled at a later date!")
        else:
            return form_date


    def clean_patient_name(self):
        """ Checks if patient name has any numbers in it"""
        pat_name = self.cleaned_data['patient_name']

        if pat_name.isalpha():
            return pat_name
        else:
            raise forms.ValidationError("Enter a valid patient name!")


    class Meta:
        model = Appointment
        fields = '__all__'