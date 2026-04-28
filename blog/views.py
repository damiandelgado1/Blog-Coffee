from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView
from .models import Blog


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