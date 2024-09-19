from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    title = "DimStore"
    slogan = "DimStore - это лучший вариант для покупки гаджетов"
    context = {"products": products,
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
