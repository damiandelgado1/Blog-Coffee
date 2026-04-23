from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Blog
from .forms import SuscribeForm


# Display all Post's
class ListBlog(ListView):
    model = Blog
    template_name = "blog/list_blog.html"
    context_object_name = "Blogs"


# See Blog detail
class DetailBlog(DetailView):
    model = Blog
    template_name = "blog/detail_blog.html"
    context_object_name = "Blog"


# Create a Blog new with Name, Image (Optional), Description, Date created
class CreateBlog(CreateView):
    model = Blog
    template_name = "blog/create_blog.html"
    fields = ("name", "image", "description", "created_at")
    success_url = reverse_lazy("blog_list")


# Modify information and data of Blog
class ModifyBlog(UpdateView):
    model = Blog
    template_name = "blog/modify_blog.html"
    fields = ("name", "description")
    success_url = reverse_lazy("blog_detail")


# Delete a Blog by Site's
class DeleteBlog(DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy("blog_list")


# Form for suscribe Blog
def form_suscribe(request):
    if request.POST:
        form = SuscribeForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data("first_name")
            last_name = form.cleaned_data("last_name")
            email = form.cleaned_data("email")

            if "@gmail.com" not in email:
                messages.error("El email no se Ingreso Correctamente")

            else:
                messages.success(request, "La suscripcion al Blog se ha hecho correctamente")
                form.save()

                context = {
                    "Nombre del Nuevo seguidor": name,
                    "Apellido": last_name,
                    "Email del Nuevo seguidor": email,
                }

                return render(request, "", context)
        
        else:
            return f"No puedes dejar el Formulario vacio"