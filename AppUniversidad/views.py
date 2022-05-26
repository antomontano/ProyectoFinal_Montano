from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppUniversidad.forms import *
# Create your views here.

def inicio(request):
    return render(request,'AppUniversidad/inicio.html')

def aboutUs(request):
    return render(request,'AppUniversidad/aboutUs.html')

def registrarme(request):
    return render(request,'AppUniversidad/registrarme.html')

def login(request):
    return render(request,'AppUniversidad/login.html')

