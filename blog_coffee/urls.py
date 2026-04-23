from django.contrib import admin
from django.urls import path, include
from .views import main_page, form_page

urlpatterns = [
    path('', main_page, name="home"),
    path('form/', form_page, name="form"),
    path('blog/', include('blog.urls', namespace="blog")),
    path('admin/', admin.site.urls),
]