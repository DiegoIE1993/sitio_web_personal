from django.db import models

# Create your models here.

class about(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='sobre_mi/', blank=True, null=True)
    #cv = acá va la hoja de vida
    
    def __str__(self):
        return self.nombre
    
    
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.titulo
    
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    link = models.URLField(blank=True, null= True)
    
    def __str__(self):
        return self.titulo
    
class ExperienciaLaboral(models.Model):
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.puesto} en {self.empresa}"
    
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"