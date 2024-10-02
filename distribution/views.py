from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from distribution.forms import ProductForm
from distribution.models import Message, Delivery


class MessageListView(ListView):
    model = Message


class DeliveryListView(ListView):
    model = Delivery


class DeliveryDetailView(DetailView):
    model = Delivery


# СДЕЛАТЬ ФОРМУ
class DeliveryCreateView(CreateView):
    model = Delivery
    form_class = ProductForm
    success_url = reverse_lazy('distribution:delivery_list')


class DeliveryUpdateView(UpdateView):
    model = Delivery
    form_class = ProductForm
    success_url = reverse_lazy('distribution:delivery_list')


class DeliveryDeleteView(DeleteView):
    model = Delivery
    success_url = reverse_lazy('distribution:delivery_list')
