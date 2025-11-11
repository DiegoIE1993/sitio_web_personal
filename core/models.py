from django.db import models

# Definición de modelos

class Profile(models.Model):
    
    #Definicion de campos del modelo profile
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, verbose_name="Profesional")
    biography = models.TextField(verbose_name="Biography")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    #cv = acá va la hoja de vida
    
    def __str__(self):
        return self.full_name
    
    
class Project(models.Model):
    #Definición campos del modelo project
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='proyectos/', blank=True, null=True, verbose_name="Image")
    link = models.URLField(blank=True, null= True, verbose_name="Project Link")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    class Meta:
        ordering = ['-created_at']
        
    
    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date_obtained = models.DateField()
    certificate_file = models.FileField(upload_to='certifications/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date_obtained']
    
    def __str__(self):
        return f"{self.title} - {self.institution}"



class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Mensaje de {self.name}"