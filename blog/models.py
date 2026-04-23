from django.db import models

# Blog information about Coffee
class Blog(models.Model):
    name = models.TextField(blank=True, default="Blog sobre Cafe", verbose_name="Blog")
    image = models.ImageField(upload_to="", blank=True, null=True)
    category = models.TextField(blank=True, default="Categoria del Blog", verbose_name="Categoria")
    content = models.TextField(blank=True, verbose_name="Descripcion del Blog creado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")

    def __str__(self):
        return f"Nuevo Blog creado sobre: {self.name} en la Fecha y Hora {self.created_at}"

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"