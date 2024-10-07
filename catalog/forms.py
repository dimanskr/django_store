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
