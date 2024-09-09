from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from django.views import View

from article_module.models import ArticleModel
from product_module.models import Product_Model
from sitesetting_module.models import SliderModel, SiteSettingModel
from user_module.models import User


class Home(View):
    def get(self, request):
        slider: SliderModel = SliderModel.objects.all()
        products_new = Product_Model.objects.all()
        articles_new = ArticleModel.objects.all()
        return render(request, 'home.html', {
            'slider': slider,
            'products_new': products_new,
            'articles_new': articles_new
        })

    def post(self, request: HttpRequest):
        search = request.POST['search']
        return redirect(reverse('search' , args=[search]))



def search_page(request, search):
    products = Product_Model.objects.filter(title__contains=search)
    return render(request, 'product_list.html', {
        'products': products
    })




def header_render_partial(request):
    if request.method == 'GET':
        settings: SiteSettingModel = SiteSettingModel.objects.first()
        return render(request, 'header.html', {
            'settings': settings
        })




def footer_render_partial(request):
    settings: SiteSettingModel = SiteSettingModel.objects.first()
    return render(request, 'footer.html', {
        'settings': settings
    })
