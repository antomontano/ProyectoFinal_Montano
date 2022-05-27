from django import forms


class inscribirmeFinales(forms.Form):
    Materia= forms.CharField(max_length=1)
    Mesa= forms.IntegerField()
    