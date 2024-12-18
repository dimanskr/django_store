from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, ProductVersionFormSet, ProductModeratorsForm
from catalog.models import Product, Version, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from catalog.services import get_categories_from_cache


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'DimStore',
        'slogan': 'DimStore - это лучший вариант для покупки гаджетов'
    }
    paginate_by = 9
    context_object_name = "products"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data['object_list']:
            active_version = Version.objects.filter(product=product, is_current_version=True).first()
            product.active_version = active_version
        return context_data

    def get_queryset(self):
        user = self.request.user

        # Модератор с правом "can_set_published" видит все продукты
        if user.has_perm('catalog.can_set_published'):
            return Product.objects.all()

        # Владелец видит свои продукты и опубликованные
        elif user.is_authenticated:
            return Product.objects.filter(Q(owner=user) | Q(is_published=True))

        # Обычный пользователь видит только опубликованные продукты
        return Product.objects.filter(is_published=True)


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:create_product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductVersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductVersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):

        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context_data['formset'] = ProductVersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductVersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (user.has_perm('catalog.can_set_published') and user.has_perm('catalog.can_edit_product_description')
                and user.has_perm('catalog.can_edit_category_product')):
            return ProductModeratorsForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class CategoryListView(ListView):
    extra_context = {'title': 'Категории товаров', }
    model = Category
    paginate_by = 9
    context_object_name = "category_list"

    def get_queryset(self):
        return get_categories_from_cache()
