from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from client.models import Client
from .forms import LoginForm
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


class MyView(View):
    def get(self, request):
        return render(request, "about.html")


class LoginView(View):
    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, 'auth/sign_in.html', context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_login = data['username']
        possword = data['password']
        user = authenticate(request, username=user_login, password=possword)
        if user is not None:
            login(request, user)
            return redirect(about)
        else:
            return HttpResponse('Неверный логин или пароль')


class LoginOutView(View):
    def get(self, request):
        logout(request)
        return redirect(about)

