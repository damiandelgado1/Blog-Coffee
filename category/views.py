from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Category


# Create new Category
class CreateCategory(CreateView):
    model = Category
    fields = ["name_category"]
    template_name = "category/create_category.html"
    success_url = reverse_lazy("home")