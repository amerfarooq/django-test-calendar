from django.shortcuts import render
from django.http import HttpResponseRedirect


def homePage(request):
    return render(request, 'home/home.html')