from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import ArticleForm
from blog.models import Article
from distribution.services import get_articles_from_cache


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        """Реализовано кэширование отдельных статей блога"""
        return get_articles_from_cache()


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        """Счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blog:blog_list")


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blog:blog_list")


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:blog_list")
