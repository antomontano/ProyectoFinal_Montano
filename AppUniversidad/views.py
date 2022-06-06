from typing import List
from msilib.schema import ListView
from django import http
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppUniversidad.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Mensaje
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

@login_required
def principal(request):
    avatar=Avatar.objects.filter(user = request.user)
    return render(request,'AppUniversidad/principal.html', {'url': avatar})
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
                auth_login(request, user)
                avatar=Avatar.objects.filter(user = user)
                if len(avatar)!=0:
                    avatar=avatar[0].avatar.url
                else:
                    avatar=""
                return render(request,'AppUniversidad/principal.html', {'url': avatar})
                
            
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
        
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():

            username = formulario.cleaned_data['username']
            formulario.save()
            return render(request,"AppUniversidad/registrarme.html" ,  {"Mensaje":"Usuario Creado"})


    else:     
        formulario = UserRegisterForm()     

    return render(request,"AppUniversidad/registrarme.html" ,  {"formulario":formulario})


#-----------------------------------------------

def editarPerfil(request):

      usuario = request.user
     
      if request.method == 'POST':
            formulario = UserEditForm(request.POST, instance=usuario) 
            if formulario.is_valid(): 

                  informacion = formulario.cleaned_data
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppUniversidad/principal.html",  {"Mensaje":"Usuario Modificado"})
      else: 
    
            formulario= UserEditForm(initial={ 'email':usuario.email}) 

    
      return render(request, "AppUniversidad/editarPerfil.html", {"formulario":formulario, "usuario":usuario})


def consulta(request):
    return render(request,'AppUniversidad/consulta.html')

#--------------------------------
def chats(request):
        return render(request, 'AppUniversidad/chats.html',
                      {'users': User.objects.exclude(username=request.user.username)})

def chat_detalle(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Mensaje.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        for message in messages:
            message.is_read=True
            message.save()
        form=MensajeFormulario()
        return render (request, 'AppUniversidad/chat_detalle.html', {'users': User.objects.exclude(username=request.user.username),
        'form':form,
        'sender':sender,
        'receiver':receiver,
        'messages': Mensaje.objects.filter(sender_id=sender, receiver_id=receiver) | 
        Mensaje.objects.filter(sender_id=receiver, receiver_id=sender)})

    else:
        form_vacio=MensajeFormulario()
        data=MensajeFormulario(request.POST)
        if data.is_valid():
            data_clean=data.cleaned_data.get('message')
            message=Mensaje(sender_id=sender, receiver_id=receiver, message=data_clean)
            message.save()
            return render(request, 'AppUniversidad/chat_detalle.html', {'users': User.objects.exclude(username=request.user.username),
            'form':form_vacio,
            'form_lleno':data,
            'sender':sender,
            'receiver':receiver,
            'messages': Mensaje.objects.filter(sender_id=sender, receiver_id=receiver) |
             Mensaje.objects.filter(sender_id=receiver, receiver_id=sender)})