from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' , 'required' : 'reguired' , 'placeholder' : 'نام' }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control' , 'required' : 'reguired' , 'placeholder' : 'ایمیل' }))
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control' , 'required' : 'reguired' , 'placeholder' : 'دیدگاه' , 'rows' : '7'}))