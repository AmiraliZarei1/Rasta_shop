from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری' , widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(label='ایمیل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ConfirmRegisterForm(forms.Form):
    code = forms.CharField(label='کد فعالسازی', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ForgetPasswordForm(forms.Form):
    email = forms.CharField(label='ایمیل', widget=forms.TextInput(attrs={'class': 'form-control'}))


class ConfirmForgetForm(forms.Form):
    code = forms.CharField(label='کد فعالسازی', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ChangePasswordForm(forms.Form):
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

