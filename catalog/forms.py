from django import forms
from .models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field, forms.DateTimeField):
                field.widget.attrs['class'] = 'form-control datetimepicker'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    prohibited_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                             'радар']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in self.prohibited_words_list:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенные слова в названии!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in self.prohibited_words_list:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенные слова в описании!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"


ProductFormset = forms.inlineformset_factory(
    Product,
    Version,
    form=VersionForm,
    extra=1)


class ProductVersionFormSet(ProductFormset):
    def clean(self):
        version_forms = self.forms
        is_latest_count = len([1 for f in version_forms if f.instance.is_current_version])
        if is_latest_count > 1:
            raise forms.ValidationError('Может быть только одна текущая версия продукта!')
        super().clean()
