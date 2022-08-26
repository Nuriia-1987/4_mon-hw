from django.shortcuts import render

# Create your views here.
from client.models import Client


def name_list(request):
    context = {}
    names1_list = Client.objects.all()
    context["names1_list"] = names1_list
    return render(request, 'name.html', context)


def clients_list(request):
    context = {}
    context["core"] = Client.objects.all()
    return render(request, 'core.html', context)
