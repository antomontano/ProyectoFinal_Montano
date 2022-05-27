from django.db import models

# Create your models here.

class Inscripcion(models.Model):
    Materia= models.CharField(max_length=1)
    Mesa= models.IntegerField()

    def __str__(self):
        return self.Materia+" "+str(self.Mesa)