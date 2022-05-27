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