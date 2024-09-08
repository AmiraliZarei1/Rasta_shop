from builtins import complex

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
# Create your views here.
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from user_module.forms import RegisterForm, LoginForm, ConfirmRegisterForm, ForgetPasswordForm, ConfirmForgetForm, \
    ChangePasswordForm
from user_module.models import User
from utils.email_service import *
from utils import random_code


class Login(View):
    def get(self, request: HttpRequest):
        login_form = LoginForm
        return render(request, 'login.html', {
            'login_form': login_form
        })

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = User.objects.filter(username=username).first()
            if user is not None:
                check = user.check_password(password)
                if check:
                    login(request, user)
                    return redirect('Home')
                else:
                    # login_form.add_error('username' , 'نام کاربری یا رمز عبور اشتباه است')
                    return render(request, 'login.html', {
                        'login_form': login_form,
                        'error': True
                    })
            else:
                # login_form.add_error('username' , 'نام کاربری یا رمز عبور اشتباه است')
                return render(request, 'login.html', {
                    'login_form': login_form,
                    'error': True
                })
        else:
            # login_form.add_error('username', 'نام کاربری یا رمز عبور اشتباه است')
            return render(request, 'login.html', {
                'login_form': login_form,
                'error': True
            })


class Register(View):
    def get(self, request: HttpRequest):
        register = RegisterForm()
        return render(request, 'register.html', {
            'register': register
        })

    def post(self, request: HttpRequest):
        register = RegisterForm(request.POST)
        if register.is_valid():
            username = register.cleaned_data.get('username')
            email = register.cleaned_data.get('email')
            password = register.cleaned_data.get('password')
            if password == password:
                user = User.objects.filter(email=email).first()
                if user is not None:
                    return render(request, 'register.html', {
                        'register': register,
                        'error': True
                    })
                else:
                    new_user = User(username=username, email=email, password=password, is_active=False,
                                    verify_code=random_code.random_number())
                    new_user.set_password(password)
                    new_user.save()
                    # new_user.generate_token()
                    send_email('تایید ایمیل', User.email, {'user': user}, 'email_template.html')
                    return redirect(reverse('confirm-register', args=[new_user.id]))
            else:
                return redirect('register')
        else:
            raise Http404('')


class ConfirmRegister(View):
    def get(self, request, id):
        user: User = User.objects.filter(id=id).first()
        if user is not None:
            if not user.is_active:
                confirm_form = ConfirmRegisterForm()
                return render(request, 'confirm_register.html', {
                    'confirm_form': confirm_form
                })
            else:
                raise Http404('user is none')


        else:
            raise Http404('testtest')

    def post(self, request, id):
        user: User = User.objects.filter(id=id).first()
        if user is not None and not user.is_active:
            confirm_form = ConfirmRegisterForm(request.POST)
            if confirm_form.is_valid():
                confirm = confirm_form.cleaned_data.get('code')
                if user.verify_code == confirm:
                    user.is_active = True
                    user.save()
                    return redirect('login')
                else:
                    return render(request, 'confirm_register.html', {
                        'confirm_form': confirm_form,
                        'error': True
                    })
            else:
                raise Http404("test")


class ForgetPassword(View):
    def get(self, request):
        forget = ForgetPasswordForm()
        return render(request, 'forget_password.html', {
            'forget_form': forget
        })

    def post(self, request):
        forget = ForgetPasswordForm(request.POST)
        if forget.is_valid():
            email = forget.cleaned_data.get('email')
            user: User = User.objects.filter(email=email).first()
            if user is not None:
                send_email('تایید ایمیل', user.email, {'user': user}, 'email_template.html')
                user.generate_token()
                user.save()
                return redirect(reverse('confirm-forget', args=[user.token]))
            else:
                # forget.add_error('email', 'هیچ کاربری با این ایمیل یافت نشد')
                return render(request, 'forget_password.html', {
                    'forget_form': forget ,
                    'error' : True
                })


class ConfirmForget(View):
    error_dict = {}

    def get(self, request, token):
        user = User.objects.filter(token=token).first()
        if user is not None:
            confirm_forget = ConfirmForgetForm()
            return render(request, 'confirm_forget.html', {
                'confirm_forget': confirm_forget
            })
        else:
            raise Http404()

    def post(self, request, token):
        user = User.objects.filter(token=token).first()
        if user is not None:
            confirm_forget = ConfirmForgetForm(request.POST)
            if confirm_forget.is_valid():
                send_email('تایید ایمیل', user.email, {'user': user}, 'email_template.html')
                confirm = confirm_forget.cleaned_data.get('code')
                if user.verify_code == confirm:
                    user.token = get_random_string(100)
                    user.save()
                    return redirect(reverse('change-password', args=[user.token, user.verify_code]))
                else:
                    confirm_forget.add_error('code', 'کد اشتباه است')
                    if str(user.id) in ConfirmForget.error_dict.keys():
                        error_num = ConfirmForget.error_dict[str(user.id)] + 1
                        if error_num > 3:
                            user.generate_token()
                            user.verify_code = random_code.random_number()
                            user.save()
                            ConfirmForget.error_dict.pop(str(user.id))
                            print(ConfirmForget.error_dict)
                            raise Http404
                        ConfirmForget.error_dict.update({str(user.id): error_num})
                    else:
                        ConfirmForget.error_dict.update({str(user.id): 1})
                    return render(request, 'confirm_forget.html', {
                        'confirm_forget': confirm_forget
                    })
            else:
                raise Http404()


class ChangePassword(View):
    def get(self, request, token, code):
        user = User.objects.filter(token=token, verify_code=code).first()
        if user is not None:
            change_form = ChangePasswordForm()
            return render(request, 'change_password.html', {
                'change_form': change_form
            })
        else:
            raise Http404()

    def post(self, request, token, code):
        user: User = User.objects.filter(token=token, verify_code=code).first()
        change_form = ChangePasswordForm(request.POST)
        if change_form.is_valid():
            password = change_form.cleaned_data.get('password')
            re_password = change_form.cleaned_data.get('re_password')
            if password == re_password:
                user.set_password(password)
                send_email('تایید ایمیل', user.email, {'user': user}, 'email_template.html')
                user.generate_token()
                user.save()
                return redirect('login')
            else:
                change_form.add_error('password', 'رمز عبور و تکرار مطابقت ندارد')
        return render(request, 'change_password.html', {
            'change_form': change_form
        })


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('Home')
