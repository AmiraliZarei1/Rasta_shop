from cProfile import label

from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100 , label='جستجو' ,widget=forms.TextInput(attrs={'class': 'form-control'}))
