from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm,ProductVersionFormSet
from catalog.models import Product, Version


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
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(UpdateView):
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


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
