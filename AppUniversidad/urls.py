from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('aboutUs', aboutUs, name= 'aboutUs'),
    path('registrarme', registrarme, name= 'registrarme'),
    path('login', login, name= 'login'),

]