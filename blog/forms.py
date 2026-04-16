from django.db import models
from django import forms

class ManageBlog(models.Form):
    name = forms.TextInput(required=True, blank=True, default="Blog sobre Cafe", verbose_name="Blog")
    image = forms.ImageField(upload_to="", blank=True, null=True)
    description = forms.Textarea(required=True, widget=forms.Textarea,blank=True, verbose_name="Descripcion del Blog creado")
    created_at = forms.DateTimeField(required=True, auto_now_add=True)