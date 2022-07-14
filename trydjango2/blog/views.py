from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView

from .models import Article
from .form import ArticleModelForm


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Article.objects.all()
