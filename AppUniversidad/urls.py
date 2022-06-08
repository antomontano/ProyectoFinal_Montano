from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('aboutUs', aboutUs, name= 'aboutUs'),
    path('registrarme', registrarme, name= 'registrarme'),
    path('login', Login_request, name= 'login'),
    path('inscripciones', LeerInscripciones, name= 'inscripciones'),
    path('inscribirmeFinales', inscribirmeFinales, name= 'inscribirmeFinales'),
    path('principal', principal, name= 'principal'),
    path('EliminarInscripcion/<id>', EliminarInscripcion, name= 'EliminarInscripcion'),
    path('logout', LogoutView.as_view(template_name="AppUniversidad/logout.html"), name= 'logout'),
    path('editarPerfil', editarPerfil, name= 'editarPerfil'),
    path('consulta', LeerConsultas, name= 'consulta'),
    path('chats/',chats, name='chats'),
    path('chats/<int:sender>/<int:receiver>/', chat_detalle, name='chat_detalle'),
    path('crearConsulta', CrearConsulta, name= 'crearConsulta'),
    path('EliminarConsulta/<id>', EliminarConsulta, name= 'EliminarConsulta'),
    path('editarConsulta/<id>', EditarConsulta, name= 'editarConsulta'),
    path('consulta/detalle/<pk>', DetalleConsulta.as_view(), name= 'detalleConsulta'),
]