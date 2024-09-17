from django.shortcuts import render
from django.views.generic import ListView

from distribution.models import Message


class MessageListView(ListView):
    model = Message




# Create your views here.
