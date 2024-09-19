from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts, product_detail, create_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path('create/', create_product, name='create_product'),
    path('contacts/', contacts, name='contacts'),
]
