from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    decripccion = models.TextField()
    enlace = models.URLField(blank=True)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo
