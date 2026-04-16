from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Blog

# Display all Post's
class ListBlog(ListView):
    model = Blog
    template_name = ""
    context_object_name = "Blogs"

# See Blog detail
class DetailBlog(DetailView):
    model = Blog
    template_name = ""
    context_object_name = "Blog"

# Create a Blog new with Name, Image (Optional), Description, Date created
@method_decorator(login_required, name="dispatch")
class CreateBlog(CreateView):
    model = Blog
    template_name = ""
    fields = ("name", "image", "description", "created_at")
    success_url = reverse_lazy("blog_list")

# Modify information and data of Blog
@method_decorator(login_required, name="dispatch")
class ModifyBlog(UpdateView):
    model = Blog
    template_name = ""
    fields = ("name", "description")
    success_url = reverse_lazy("blog_detail")

# Delete a Blog by Site's
@method_decorator(login_required, name="dispatch")
class DeleteBlog(DeleteView):
    model = Blog
    template_name = ""
    success_url = reverse_lazy("blog_list")