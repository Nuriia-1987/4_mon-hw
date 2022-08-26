from django.shortcuts import render, HttpResponse

# Create your views here.
from client.models import Client
from .models import Bottle


def contacts(request):
    return render(request, 'core/contacts.html')


def about(request):
    return render(request, 'about.html')


def makers_list(reguest):
    context = {}
    bottles_list = Bottle.objects.all()
    context['bottles_list'] = bottles_list
    return render(reguest, 'makers.html', context)
