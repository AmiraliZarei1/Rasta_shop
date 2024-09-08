from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.




def product_list(request) :
    products_new = Product_Model.objects.all()
    return render(request , 'product_list.html' , {
       'products_new' : products_new

    })


def product_detail(request , slug):
    products = Product_Model.objects.get(slug=slug)
    comments:ProductComment_Model = ProductComment_Model.objects.filter(product_id=products.id , parent=None)
    return render(request, 'product_detail.html', {
        'products': products ,
        'comments': comments
    })


def comments(request):
    if request.user.is_authenticated:
        product_id = request.GET.get('product_id')
        hidden_input = request.GET.get('parent_id')
        product = Product_Model.objects.filter(id=product_id).first()
        if product is not None:
            if hidden_input:
                user_id = request.user.id
                comment = request.GET.get('text')
                new_comment = ProductComment_Model(product_id=product_id, user_id=user_id , text=comment , parent_id=hidden_input)
                new_comment.save()
                return HttpResponse("success")
            else:
                user_id = request.user.id
                comment = request.GET.get('text')
                new_comment = ProductComment_Model(product_id=product_id, user_id=user_id , text=comment , parent_id=None)
                new_comment.save()
                return HttpResponse("success")


        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")