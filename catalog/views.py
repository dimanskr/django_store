from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # выводим в консоль информацию о пользователе
        print(f"Пользователь {name} оставил комментарий '{message}'"    
              f" и просил связаться с ним по телефону {phone} ")
    return render(request, 'catalog/contacts.html')
