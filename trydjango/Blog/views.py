from django.shortcuts import render
from .models import Article
from .form import ArticleForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class ArticleCreateView(CreateView):
    queryset = Article.objects.all()
    form_class = ArticleForm
    template_name = 'Blog/article_create.html'


class ArticleUpdateView(UpdateView):
    queryset = Article.objects.all()
    form_class = ArticleForm
    template_name = 'Blog/article_update.html'


class ArticleDeleteView(DeleteView):
    queryset = Article.objects.all()
    template_name = 'Blog/article_delete.html'
    success_url = '/blog/'

