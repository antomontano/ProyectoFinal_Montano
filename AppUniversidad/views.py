from django import http
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppUniversidad.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def inicio(request):
    return render(request,'AppUniversidad/inicio.html')

def aboutUs(request):
    return render(request,'AppUniversidad/aboutUs.html')

def registrarme(request):
    return render(request,'AppUniversidad/registrarme.html')

def login(request):
    return render(request,'AppUniversidad/login.html')

def inscripciones(request):
    return render(request,'AppUniversidad/inscripciones.html')

def inscribirmeFinales(request):
    if request.method == 'POST':
        inscripcion=Inscripcion(Materia=request.POST['Materia'], Mesa=request.POST['Mesa'])
        inscripcion.save()
        return render(request,'AppUniversidad/inscribirmeFinales.html')
    return render(request,'AppUniversidad/inscribirmeFinales.html')

def principal(request):
    return render(request,'AppUniversidad/principal.html')
#---------------------

def LeerInscripciones(request):
    inscripciones=Inscripcion.objects.all()
    return render(request, 'AppUniversidad/inscripciones.html', {'inscripciones':inscripciones})

def EliminarInscripcion(request, id):
    inscripcion=Inscripcion.objects.get(id=id)
    inscripcion.delete()
    inscripciones=Inscripcion.objects.all()
    return render(request, 'AppUniversidad/inscripciones.html', {'inscripciones':inscripciones})

#-----------------LOGIN-----------------------------
def Login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request=request, data=request.POST)
       
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')


            user=authenticate(username=usuario, password=clave)
            
            if user is not None:
                login(request)
                return render(request, 'AppUniversidad/principal.html')
            
            else:
                return render(request, 'AppUniversidad/login.html', {'Mensaje': 'Usuario incorrecto, intente nuevamente'})
      
        else:
            return render(request, 'AppUniversidad/login.html', {'Mensaje': 'Formulario inválido'})
    
    else:
        formulario=AuthenticationForm()
        return render(request, 'AppUniversidad/login.html', {'formulario': formulario})


#---------------REGISTRO-----------------

def registrarme(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'AppUniversidad/login.html', {'Mensaje': f'Usuario {username} creado exitosamente'})
        else:
            return render(request, 'AppUniversidad/login.html', {'Mensaje': 'No se pudo crear el usuario'})
    else:
        formulario = UserCreationForm()
        return render(request, 'AppUniversidad/registrarme.html', {'formulario': formulario})