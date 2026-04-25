from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, ListView, DetailView
from .models import Blog
from .forms import SuscribeForm


# Display all Post's
class ListBlog(ListView):
    model = Blog
    template_name = "blog/list_blog.html"
    context_object_name = "blogs"


# See Blog detail
class DetailBlog(DetailView):
    model = Blog
    template_name = "blog/detail_blog.html"
    context_object_name = "blog"


# Create a Blog new with Name, Image (Optional), Description, Date created
class CreateBlog(CreateView):
    model = Blog
    template_name = "blog/create_blog.html"
    fields = ["name", "image", "category", "content"]
    success_url = reverse_lazy("blog:blog_list")


# Delete a Blog by Site's
class DeleteBlog(DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy("home")


# Form for suscribe Blog
def form_suscribe(request):
    if request.method == "POST":
        form = SuscribeForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]

            if "@gmail.com" not in email:
                messages.error(request, "El email no se Ingreso Correctamente")

            else:
                messages.success(request, "La suscripcion al Blog se ha hecho correctamente")
                form.save()
        
    else:
        form = SuscribeForm()
    
    return render(request, "home/form.html", {"form": form})