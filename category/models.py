from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=30, default="Categoria del Blog", verbose_name="Categoria")

    def __str__(self):
        return f"{self.name_category}"

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"