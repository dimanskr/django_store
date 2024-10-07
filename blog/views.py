from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(ListView):
    extra_context = {
        'title': 'Новости',
    }
    model = Article
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        new_article = form.save(commit=False)
        new_article.slug = slugify(new_article.title)
        new_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.object.slug})


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        new_article = form.save(commit=False)
        new_article.slug = slugify(new_article.title)
        new_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.object.slug})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')

