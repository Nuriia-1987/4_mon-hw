from django.shortcuts import render, HttpResponse
from client.models import Client, Order
from .forms import OrderForm, ClientForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ClientListView(ListView):
    model = Client
    template_name = 'clients.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = "client_info.html"


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    fields = ['name', 'address']
    success_url = '/clients/'


class CreateOrderView(View):
    def post(self, request):
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.contacts = data["contacts"]
        order.description = data["description"]
        order.save()
        return HttpResponse("Форма обработана")

    def get(self, request):
        return render(request, 'core/order_form.html')


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_object.html'


class CreateOrderDjangoView(CreateView):
    model = Order
    template_name = 'order_djangoform.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['our_number'] = 7
        return context


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'


class ClientOrderList(ListView):
    model = Order
    template_name = 'order_list.html'
