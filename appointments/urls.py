from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createAppointments),
    path('display', views.showAppointments),
    path('', views.home),
]
