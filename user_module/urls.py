from django.urls import path
from .views import *



urlpatterns = [
    path('register/' , Register.as_view() , name='register'),
    path('confirm-register/<id>/' , ConfirmRegister.as_view() , name='confirm-register') ,
    path('login/' , Login.as_view() , name='login') ,
    path('forget-password/' , ForgetPassword.as_view() , name='forget-password') ,
    path('confirm-forget/<token>/' , ConfirmForget.as_view() , name='confirm-forget') ,
    path('change-password/<token>/<code>/' , ChangePassword.as_view() , name='change-password') ,
    path('logout/' , Logout.as_view() , name='logout')
]