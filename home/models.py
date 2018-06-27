from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    
    userTypes = (
        ('S', 'Supervisor'),
        ('D', 'Doctor'),
        ('FD', 'Front-desk'),
    )

    userType = models.CharField(max_length=1, choices=userTypes)
