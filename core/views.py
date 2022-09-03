from django.shortcuts import render, HttpResponse

# Create your views here.
from client.models import Client
from .models import Bottle, BottleCount
from django.views import View
from django.views.generic import ListView


def contacts(request):
    return render(request, 'core/contacts.html')


def about(request):
    return render(request, 'about.html')


class MakerListView(ListView):
    model = Bottle
    template_name = 'makers.html'

# def makers_list(request):
#     context = {}
#     bottles_list = Bottle.objects.all()
#     context['bottles_list'] = bottles_list
#     return render(request, , context)


class MyView(View):
    def get(self, request):
        return render(request, "about.html")
