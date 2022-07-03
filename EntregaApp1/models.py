from django.db import models

# Create your models here.
class Block(models.Model):
    titulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=120)
    fecha_creaccion=models.DateField(null=True)