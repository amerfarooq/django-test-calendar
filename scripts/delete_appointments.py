from appointments.models import Appointment

def run():
    Appointment.objects.all().delete()