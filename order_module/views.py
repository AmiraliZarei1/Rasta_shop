
from itertools import count

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from order_module.models import Order, OrderDetail
from product_module.models import Product_Model


# Create your views here.

@method_decorator(login_required , name='dispatch')
class UserBasket(View):
    def get(self, request):
        user_id = request.user.id
        order:Order = Order.objects.filter(user_id=user_id).first()
        details = OrderDetail.objects.filter(order_id=order.id)
        return render(request , 'user_basket.html' , {
            'order': order ,
            'details': details
        })




@login_required
def add_to_order(request):
    product_id = request.GET.get('product_id')
    count = int(request.GET.get('count'))
    if request.user.is_authenticated:
        user = request.user.id
        product:Product_Model = Product_Model.objects.filter(id=product_id).first()
        if product is not None:
            if count <= product.count:
                order , created = Order.objects.get_or_create(is_paid=False , user_id=user)
                detail = order.orderdetail_set.filter(product_id=product_id).first()
                if detail is not None:
                    detail.count += count
                    detail.final_price = int(detail.count) * int(product.price)
                    detail.save()
                else:
                    final_price = int(product.price) * int(count)
                    new_detail = OrderDetail(order_id=order.id , product_id=product_id , count=count , final_price=final_price)
                    new_detail.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error-count'})

        else:
            return JsonResponse({'status': 'not-login'})
    else:
        return JsonResponse({'status' : 'not-login'})