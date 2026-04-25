from django.db import models

# Blog information about Coffee
class Blog(models.Model):
    name = models.CharField(max_length=50, blank=True, default="Blog sobre Cafe", verbose_name="Blog")
    image = models.ImageField(upload_to="", blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, default="Categoria del Blog", verbose_name="Categoria")
    content = models.TextField(blank=True, verbose_name="Descripcion del Blog creado")
    created_at = models.DateTimeField(max_length=50, auto_now_add=True, verbose_name="Fecha de Creacion")

    def __str__(self):
        return f"Nuevo Blog creado sobre: {self.name} en la Fecha y Hora {self.created_at}"