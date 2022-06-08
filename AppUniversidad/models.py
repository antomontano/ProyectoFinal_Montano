from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Inscripcion(models.Model):
    Materia= models.CharField(max_length=1)
    Mesa= models.IntegerField()

    def __str__(self):
        return self.Materia+" "+str(self.Mesa)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)


class Mensaje(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)


#---------------------------------

class Consulta(models.Model):
    fecha=models.DateField(default=timezone.now)
    titulo=models.CharField(max_length=70)
    cuerpo=models.CharField(max_length=1000)
    ejercicio=models.ImageField(blank=True, upload_to='ejercicio')
    def __str__(self):
        return f"Consulta: {self.titulo}"