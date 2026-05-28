from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import main_page, form_suscribe

urlpatterns = [
    path('', main_page, name="home"),
    path('blog/', include('blog.urls', namespace="blog")),
    path('form/', form_suscribe, name="form_suscribe"),
    path('category/', include('category.urls', namespace="category")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)