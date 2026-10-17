from django.db import models

# Create your models here.
from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return f"{self.nombre}: {self.texto}"