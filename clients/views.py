from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Client


def name_list(request):
    context = {}
    names1_list = Client.objects.all()
    context["names1_list"] = names1_list
    return render(request, 'name.html', context)


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'clients/contacts.html')


def clients_list(request):
    context = {}
    context["clients"] = Client.objects.all()
    return render(request, 'clients.html', context)
