from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import *


class ArticleListView(View):
    def get(self , request):
        article:ArticleModel = ArticleModel.objects.filter(is_active=True)
        return render(request , 'article_list.html' , {
            'article' : article
        })

class ArticleDetailView(View):
    def get(self , request , id):
        article:ArticleModel = ArticleModel.objects.filter(id=id).first()
        return render(request , 'article_detail.html' , {
            'article' : article
        })