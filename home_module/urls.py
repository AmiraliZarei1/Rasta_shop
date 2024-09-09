from django.urls import path
from .views import *

urlpatterns = [
    path('' , Home.as_view() , name='Home') ,
    path('search/<search>/' , search_page , name='search')
]