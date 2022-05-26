from django import forms


class CarrerasFormulario(forms.Form):
    Facultad= forms.CharField(max_length=50)
    NombreCarrera= forms.CharField(max_length=50)

class CursosFormulario(forms.Form):
    Año= forms.IntegerField()
    Turno= forms.CharField(max_length=50)

class DatosFormulario(forms.Form):
    Nombre= forms.CharField(max_length=50)
    Apellido= forms.CharField(max_length=50)
    DNI= forms.IntegerField()
    