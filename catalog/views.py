from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # выводим в консоль информацию о пользователе
        print(f"Пользователь {name} оставил комментарий '{message}'"
              f" и просил связаться с ним по телефону {phone} ")
    return render(request, 'catalog/contacts.html')
