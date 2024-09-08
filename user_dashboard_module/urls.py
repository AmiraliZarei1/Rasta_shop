from django.urls import path
from .views import *

urlpatterns = [
    path('', MainDashboardView.as_view() , name='main-dashboard'),
    path('edit-user/' , EditUserDashboardView.as_view() , name='edit-user') ,
    path('change-password-dash' , ChangePasswordDashView.as_view() , name='change-pass-dash')
]