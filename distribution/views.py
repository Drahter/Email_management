from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
    fields = ['email_client', 'message', 'period', 'message', 'is_active']
    success_url = reverse_lazy('distribution:delivery_list')


class DeliveryUpdateView(UpdateView):
    model = Delivery
    fields = ['email_client', 'message', 'period', 'message', 'is_active', 'status']
    success_url = reverse_lazy('distribution:delivery_list')


class DeliveryDeleteView(DeleteView):
    model = Delivery
    success_url = reverse_lazy('distribution:delivery_list')
