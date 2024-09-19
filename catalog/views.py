from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from catalog.forms import ProductForm
from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = "DimStore"
    slogan = "DimStore - это лучший вариант для покупки гаджетов"
    context = {"products": page_obj,
               "title": title,
               "slogan": slogan}
    return render(request, "catalog/product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = "DimStore"
    slogan = "DimStore - это лучший вариант для покупки гаджетов"
    context = {"product": product,
               "title": title,
               "slogan": slogan}
    return render(request, "catalog/product_detail.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # выводим в консоль информацию о пользователе
        print(f"Пользователь {name} оставил комментарий '{message}'"
              f" и просил связаться с ним по телефону {phone} ")
    title = "Контакты"
    context = {"title": title}
    return render(request, 'catalog/contacts.html', context)


def create_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Товар успешно добавлен!')
        form = ProductForm()  # Очищаем форму после сохранения

    return render(request, 'catalog/create_product.html', {'form': form})
