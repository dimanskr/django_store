from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'DimStore',
        'slogan': 'DimStore - это лучший вариант для покупки гаджетов'
    }
    paginate_by = 9
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'DimStore',
        'slogan': 'DimStore - это лучший вариант для покупки гаджетов'
    }
    context_object_name = "product"


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, *args, **kwargs):
        # Обрабатываем POST запрос
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Выводим информацию из post в консоль
        print(f"Пользователь {name} оставил комментарий '{message}'"
              f" и просил связаться с ним по телефону {phone} ")

        # Возвращаем ответ
        context = self.get_context_data()
        return self.render_to_response(context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('blog:create_product')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Товар успешно добавлен!')
        # Очищаем форму после сохранения, перенаправляем обратно на создание
        return response
