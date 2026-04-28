from django.shortcuts import render
from blog.models import Blog
from blog.forms import SuscribeForm
from django.contrib import messages

# Display Main Page of the Blog
def main_page(request):
    form = SuscribeForm()
    blogs = Blog.objects.all()
    return render(request, "home/home.html", {"form": form, "blogs": blogs})


# Filter Blog by category
def filter_category(request):
    category = Blog.objects.get(category=category)
    blogs = Blog.objects.all()

    return render(request, "blog/list_blog.html", {"blogs": blogs, "categoria": category})


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