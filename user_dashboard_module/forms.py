from django import forms

from user_module.models import User


class EditDashboardForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username' , 'email' , 'avatar']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control' , 'style' : 'margin:5px'}) ,
            'last_name': forms.TextInput(attrs={'class': 'form-control' , 'style' : 'margin:5px'}) ,
            'username' : forms.TextInput(attrs={'class': 'form-control' , 'style' : 'margin:5px'}) ,
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'style' : 'margin:5px'}) ,
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'style': 'margin:5px'})
        }



class ChangePasswordDashboardForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder' : 'رمز عبور قدیم'}))
    new_pass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder' : 'رمز عبور جدید'}))
    new_pass_again = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder' : 'تکرار رمز عبور جدید'}))
