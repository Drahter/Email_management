from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from distribution.forms import DeliveryForm, MessageForm, ClientForm
from distribution.models import Message, Delivery, Client


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('distribution:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('distribution:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('distribution:message_list')


class DeliveryListView(ListView):
    model = Delivery


class DeliveryDetailView(DetailView):
    model = Delivery


class DeliveryCreateView(CreateView):
    model = Delivery
    form_class = DeliveryForm
    success_url = reverse_lazy('distribution:delivery_list')


class DeliveryUpdateView(UpdateView):
    model = Delivery
    form_class = DeliveryForm
    success_url = reverse_lazy('distribution:delivery_list')


class DeliveryDeleteView(DeleteView):
    model = Delivery
    success_url = reverse_lazy('distribution:delivery_list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('distribution:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('distribution:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('distribution:client_list')
