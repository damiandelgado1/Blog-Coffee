from django.db import models
from django import forms

class SuscribeForm(models.Form):
    first_name = forms.CharField(max_length=50, required=True, verbose_name="Nombre")
    last_name = forms.CharField(max_length=50, required=True, verbose_name="Apellido")
    email = forms.EmailField(required=True, verbose_name="Email")