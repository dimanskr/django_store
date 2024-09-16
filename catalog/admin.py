from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
    )
    list_display_links = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "preview",
        "price",
        "category",
    )
    list_editable = (
        "preview",
        "price",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )
    list_display_links = ("name",)
