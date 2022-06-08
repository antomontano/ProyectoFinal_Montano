from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppUniversidad.models import Mensaje
from .models import Consulta
from django.utils import timezone

class inscribirmeFinales(forms.Form):
    Materia= forms.CharField(max_length=1)
    Mesa= forms.IntegerField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    last_name = forms.CharField()
    first_name = forms.CharField()

   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}


class MensajeFormulario(forms.Form):
    message=forms.CharField(label="")

    class Meta:
        model=Mensaje
        fields=['sender','receiver','message','is_read']



class ConsultaFormulario(forms.Form):
    fecha=forms.DateTimeField(initial=timezone.now)
    titulo=forms.CharField(max_length=70)
    cuerpo=forms.CharField(max_length=1000)
    ejercicio=forms.ImageField()

    class Meta:
        model=Consulta
        fields=['fecha','titulo','cuerpo','ejercicio']
        help_texts={k:"" for k in fields}