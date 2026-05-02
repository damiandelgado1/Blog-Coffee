from django.contrib import admin
from category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_category"]
    search_fields = ["name_category"]
    list_filter = ["name_category"]