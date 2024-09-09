from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import logout
from user_module.models import User
from .forms import *

# Create your views here.


@method_decorator(login_required , name='dispatch')
class MainDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user:User = request.user
            return render(request , 'dashboard_template.html' , {
                'user' : user
            })
        else:
            raise Http404("You are not logged in")


@method_decorator(login_required , name='dispatch')
class EditUserDashboardView(View):
    def get(self, request):
        user = request.user
        edit_form = EditDashboardForm(instance=user)
        return render(request , 'edit_user_dashboard.html' , {
            'edit_form' : edit_form ,
            'user' : user
        })

    def post(self, request):
        user = request.user
        edit_form = EditDashboardForm(request.POST , request.FILES , instance=user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        return render(request , 'edit_user_dashboard.html' , {
            'edit_form' : edit_form
        })



@method_decorator(login_required , name='dispatch')
class ChangePasswordDashView(View):
    def get(self, request):
        user:User = request.user
        change_pass_form = ChangePasswordDashboardForm()
        return render(request , 'change_pass_dashboard.html' , {
            'change_pass_form' : change_pass_form ,
            'user' : user
        })
    def post(self, request):
        change_pass_form = ChangePasswordDashboardForm(request.POST)
        if change_pass_form.is_valid():
            user = request.user
            old_pass = change_pass_form.cleaned_data.get('old_pass')
            if user.check_password(old_pass):
                new_pass = change_pass_form.cleaned_data.get('new_pass')
                new_pass_again = change_pass_form.cleaned_data.get('new_pass_again')
                if new_pass == new_pass_again:
                    user.set_password(new_pass)
                    user.save()
                else:
                    change_pass_form.add_error('new_pass_again' , 'رمز عبور جدید و تکرار رمز عبور جدید مطابقت ندارند')
                    return render(request, 'change_pass_dashboard.html', {
                        'change_pass_form': change_pass_form
                    })
            else:
                change_pass_form.add_error('old_pass', 'رمز عبور قبلی نادرست است')
                return render(request, 'change_pass_dashboard.html', {
                    'change_pass_form': change_pass_form
                })
        else:
            raise Http404('you are not logged in')

        return render(request , 'change_pass_dashboard.html' , {
            'change_pass_form' : change_pass_form
        })



@login_required
def main_dashboard(request):
    user = request.user
    return render(request , 'dashboard_template.html' , {
        'user' : user
    })