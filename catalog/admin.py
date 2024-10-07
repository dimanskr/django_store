from django.contrib import admin
from catalog.models import Product, Category, Contact, Version


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
    ordering = ("-created_at",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone",
        "address",
    )
    search_fields = (
        "name",
        "address",
    )
    list_display_links = ("name",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "version_number",
        "name",
        "is_current_version",
    )
    list_filter = ("product",)
