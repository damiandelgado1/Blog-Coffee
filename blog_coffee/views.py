from django.shortcuts import render
from blog.models import Blog
from blog.forms import SuscribeForm

# Display Main Page of the Blog
def main_page(request):
    form = SuscribeForm()
    blogs = Blog.objects.all()
    return render(request, "home/home.html", {"form": form, "blogs": blogs})