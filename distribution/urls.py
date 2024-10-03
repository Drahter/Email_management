from django.urls import path
from distribution.apps import DistributionConfig
from distribution.views import MessageListView, DeliveryListView, DeliveryDetailView, DeliveryUpdateView, \
    DeliveryDeleteView, DeliveryCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView, ClientListView, \
    ClientDeleteView, ClientUpdateView, ClientDetailView, ContactsView, MessageCreateView, ClientCreateView

app_name = DistributionConfig.name

urlpatterns = [
    path('', DeliveryListView.as_view(), name='delivery_list'),
    # path('deliveries/', DeliveryListView.as_view(), name='delivery_list'),
    path('deliveries/create/', DeliveryCreateView.as_view(), name='delivery_create'),
    path('deliveries/<int:pk>/', DeliveryDetailView.as_view(), name='delivery_detail'),
    path('deliveries/<int:pk>/update/', DeliveryUpdateView.as_view(), name='delivery_update'),
    path('deliveries/<int:pk>/delete/', DeliveryDeleteView.as_view(), name='delivery_delete'),

    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('contacts/', ContactsView.as_view(), name='contacts'),
]
