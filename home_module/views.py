from django.db.models import Q
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from article_module.models import ArticleModel
from product_module.forms import SearchForm
from product_module.models import Product_Model
from sitesetting_module.models import SliderModel, SiteSettingModel
# from sitesetting_module.models import SiteSettingModel , SliderModel
from user_module.models import User


class Home(View):
    def get(self , request):
        slider:SliderModel = SliderModel.objects.all()
        products_new = Product_Model.objects.all()
        articles_new = ArticleModel.objects.all()
        return render(request , 'home.html' , {
            'slider' : slider ,
            'products_new' : products_new ,
            'articles_new' : articles_new
        })

    # def post(self , request:HttpRequest):
    #     search = request.POST['search']
    #
    #     return redirect(reverse('search' , args=[search]))
    #


def search_page(request):
    form = SearchForm()
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product_Model.objects.filter(title__icontains=query) | Product_Model.objects.filter(title__icontains=query)

    return render(request , 'search.html' , {
        'form' : form,
        'results' : results
    })






def header_render_partial(request):
    settings:SiteSettingModel = SiteSettingModel.objects.first()
    search_form = SearchForm()
    return render(request , 'header.html' , {
        'settings' : settings ,
        'search_form' : search_form
    })


def footer_render_partial(request):
    settings:SiteSettingModel = SiteSettingModel.objects.first()
    return render(request , 'footer.html' , {
        'settings' : settings
    })