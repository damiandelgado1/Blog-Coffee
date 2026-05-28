from django.db import models
from category.models import Category

# Blog information about Coffee
class Blog(models.Model):
    name = models.CharField(max_length=50, blank=True, default="Blog sobre Cafe", verbose_name="Blog")
    image = models.ImageField(upload_to="", blank=True)
    preview = models.TextField(verbose_name="Contenido de Previsualizacion")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs", verbose_name="Categoria del Blog")
    content = models.TextField(blank=True, verbose_name="Descripcion del Blog creado")
    created_at = models.DateTimeField(max_length=50, auto_now_add=True, verbose_name="Fecha de Creacion")

    def __str__(self):
        return f"Nuevo Blog creado sobre: {self.name} en la Fecha y Hora {self.created_at}"