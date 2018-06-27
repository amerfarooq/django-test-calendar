from django.db import models

class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)

    def __str__(self):
        return self.doc_name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appt_date = models.DateField()
    appt_time = models.TimeField()
   
    def __str__(self):
        return f'{self.patient_name} {self.doc_name} {self.appt_date}'

