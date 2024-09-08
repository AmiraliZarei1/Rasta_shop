from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    re_path(r'detail/(?P<slug>[-\w]+)/', product_detail, name='product_detail'),
    path('send-comment/' , comments)
]
