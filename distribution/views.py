from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from distribution.forms import DeliveryForm, MessageForm, ClientForm
from distribution.models import Message, Delivery, Client, SendAttempt


class MessageListView(ListView):
    model = Message

    ordering = ['pk']


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

    #    def get_queryset(self):
    #        return Message.objects.filter(owner=self.request.user)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MessageForm
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('distribution:message_list')


class DeliveryListView(ListView):
    model = Delivery

    ordering = ['pk']


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
        if user == self.object.owner or user.is_superuser:
            return DeliveryForm
        raise PermissionDenied


class DeliveryDeleteView(LoginRequiredMixin, DeleteView):
    model = Delivery
    success_url = reverse_lazy('distribution:delivery_list')


class ClientListView(ListView):
    model = Client

    ordering = ['pk']


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


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('distribution:client_list')


class ContactsView(TemplateView):
    template_name = 'distribution/contacts.html'


class SendAttemptListView(ListView):
    model = SendAttempt

    ordering = ['pk']


class DeliveryManagementView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'distribution/management_list.html'
    permission_required = 'distribution.can_view_deliveries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Delivery.objects.all().order_by('pk')
        return context


def delivery_activity(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    delivery.is_active = not delivery.is_active
    delivery.save()
    return redirect(reverse('distribution:manage_delivery'))
