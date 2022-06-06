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
    path('consulta', consulta, name= 'consulta'),
    path('chats/',chats, name='chats'),
    path('chats/<int:sender>/<int:receiver>/', chat_detalle, name='chat_detalle'),
]