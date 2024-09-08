from django.urls import path
from .views import *


urlpatterns = [
    path('add-to-order/' , add_to_order) ,
    path('user-basket/' , UserBasket.as_view() , name='user-basket')
]