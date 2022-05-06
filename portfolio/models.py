# Django
from django.db import models
# Cloudinary
from cloudinary.models import CloudinaryField

class Project(models.Model):
    """Model Project"""
    title = models.CharField(max_length=200, verbose_name="Título del proyecto")
    description = models.TextField(max_length=200, verbose_name="Descripción del proyecto")
    image = CloudinaryField('imagen', blank=True, null=True, folder="media/projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del proyecto")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización del proyecto")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title