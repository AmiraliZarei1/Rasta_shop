from django.shortcuts import render

# Create your views here.
from django.views import View

from article_module.models import ArticleModel
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



def header_render_partial(request):

    settings:SiteSettingModel = SiteSettingModel.objects.first()
    return render(request , 'header.html' , {
        'settings' : settings
    })


def footer_render_partial(request):
    settings:SiteSettingModel = SiteSettingModel.objects.first()
    return render(request , 'footer.html' , {
        'settings' : settings
    })