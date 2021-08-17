from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
from blog.models import Article


class ArticleList(ListView):
    model = Article

