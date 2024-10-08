from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from distribution.forms import DeliveryForm, MessageForm, ClientForm
from distribution.models import Message, Delivery, Client, SendAttempt


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('distribution:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('distribution:message_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MessageForm
        raise PermissionDenied


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('distribution:message_list')


class DeliveryListView(ListView):
    model = Delivery


class DeliveryDetailView(LoginRequiredMixin, DetailView):
    model = Delivery


class DeliveryCreateView(CreateView):
    model = Delivery
    form_class = DeliveryForm
    success_url = reverse_lazy('distribution:delivery_list')

    def form_valid(self, form):
        delivery = form.save()
        user = self.request.user
        delivery.owner = user
        delivery.save()

        return super().form_valid(form)


class DeliveryUpdateView(UpdateView):
    model = Delivery
    form_class = DeliveryForm
    success_url = reverse_lazy('distribution:delivery_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return DeliveryForm
        raise PermissionDenied


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

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('distribution:client_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ClientForm
        raise PermissionDenied


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('distribution:client_list')


class ContactsView(TemplateView):
    template_name = 'distribution/contacts.html'


class SendAttemptListView(ListView):
    model = SendAttempt
