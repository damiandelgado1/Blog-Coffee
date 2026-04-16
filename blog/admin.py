from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "description", "created_at"]
    search_fields = ["name"]
    list_filter = ["name", "created_at"]