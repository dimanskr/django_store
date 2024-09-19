from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'preview', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # добавление стилей bootstrap в форму добавления товара
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
