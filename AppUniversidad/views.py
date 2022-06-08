from typing import List
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
from .models import Consulta
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

# Create your views here.

def inicio(request):
    return render(request,'AppUniversidad/inicio.html')

def aboutUs(request):
    return render(request,'AppUniversidad/aboutUs.html')

def registrarme(request):
    return render(request,'AppUniversidad/registrarme.html')

def login(request):
    return render(request,'AppUniversidad/login.html')

@login_required
def inscripciones(request):
    return render(request,'AppUniversidad/inscripciones.html')

@login_required
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

@login_required
def LeerInscripciones(request):
    inscripciones=Inscripcion.objects.all()
    return render(request, 'AppUniversidad/inscripciones.html', {'inscripciones':inscripciones})

@login_required
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
@login_required
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



#---------------------------------------------------
@login_required
def LeerConsultas(request):
    consultas=Consulta.objects.all()
    return render(request, 'AppUniversidad/consulta.html', {'consultas':consultas})

@login_required
def CrearConsulta(request):
    if request.method == 'POST':

            formulario = ConsultaFormulario(request.POST)

            if formulario.is_valid():

                  informacion = formulario.cleaned_data

                  consulta = Consulta(fecha=informacion['fecha'], titulo=informacion['titulo'], cuerpo=informacion['cuerpo'], ejercicio=informacion['ejercicio']) 

                  consulta.save()

                  return render(request, "AppUniversidad/consulta.html")

    else: 

            formulario= ConsultaFormulario()

    return render(request, "AppUniversidad/crearConsulta.html", {"formulario":formulario})

@login_required
def EliminarConsulta(request, id):
    consulta=Consulta.objects.get(id=id)
    consulta.delete()
    consultas=Consulta.objects.all()
    contexto={'consultas':consultas}
    return render(request,'AppUniversidad/consulta.html', contexto)


@login_required
def EditarConsulta(request, id):
    consulta=Consulta.objects.get(id=id)
    if request.method == 'POST':
        formulario = ConsultaFormulario(request.POST)
        if formulario.is_valid():

            informacion = formulario.cleaned_data
                  
            consulta.cuerpo = informacion['cuerpo']
            consulta.ejercicio = informacion['ejercicio']

            consulta.save()

            consultas=Consulta.objects.all()
            contexto={'consultas':consultas}
            return render(request,'AppUniversidad/consulta.html', contexto)
    else: 
            formulario= ConsultaFormulario(initial={'titulo': consulta.titulo, 'cuerpo': consulta.cuerpo, 'ejercicio':consulta.ejercicio}) 

    return render(request, "AppUniversidad/editarConsulta.html", {"formulario":formulario, "id":id})




#------------------------------------------------------------------
class DetalleConsulta(DetailView):

      model = Consulta
      template_name = "AppUniversidad/detalleConsulta.html"