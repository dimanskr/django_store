from django import forms

from blog.models import Article
from catalog.forms import StyleFormMixin


class ArticleForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'preview', 'is_published')
