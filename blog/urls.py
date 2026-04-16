from django.contrib import admin
from django.urls import path
from .views import ListBlog, DetailBlog, CreateBlog, ModifyBlog, DeleteBlog

app_name = "blog"

urlpatterns = [
    path('list/', ListBlog.as_view(), name="blog_list"),
    path('detail/', DetailBlog.as_view(), name="blog_detail"),
    path('create/', CreateBlog.as_view(), name="create_blog"),
    path('update/', ModifyBlog.as_view(), name="modify_blog"),
    path('delete/', DeleteBlog.as_view(), name="deelte_blog"),
    path('admin/', admin.site.urls),
]