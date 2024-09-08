from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from contact_module.models import ContactModel
from .forms import *


def contact_us_view(request:HttpRequest):
    if request.method == 'GET' :
        contact = ContactForm
        return render(request , 'contact_us.html' , {
            'contact' : contact
    })
    elif request.method == 'POST' :
        contact = ContactForm(request.POST)
        if contact.is_valid():
            name = contact.cleaned_data.get('name')
            email = contact.cleaned_data.get('email')
            text = contact.cleaned_data.get('text')
            new_message = ContactModel(name=name , email=email , text=text)
            new_message.save()
            return render(request, 'contact_us.html', {
                'contact': contact
            })
        return render(request, 'contact_us.html', {
                'contact': contact
            })

