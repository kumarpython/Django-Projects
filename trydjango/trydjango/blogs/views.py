from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .form import ArticleModelForm
from  django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id=self.kwargs.get('id')
        return get_object_or_404(Article,id=id)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        id=self.kwargs.get('id')
        return get_object_or_404(Article,id=id)

    def get_success_url(self):
        return reverse('blogs:blogs')