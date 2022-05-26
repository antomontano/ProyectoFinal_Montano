from django.db import models

# Create your models here.

class Inscripcion(models.Model):
    Materia= models.CharField(max_length=1)
    Mesa= models.IntegerField()