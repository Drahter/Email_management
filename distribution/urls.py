from django.urls import path
from distribution.apps import DistributionConfig
from distribution.views import MessageListView, DeliveryListView, DeliveryDetailView, DeliveryUpdateView, \
    DeliveryDeleteView, DeliveryCreateView

app_name = DistributionConfig.name

urlpatterns = [
    path('', DeliveryListView.as_view(), name='delivery_list'),
    # path('deliveries/', DeliveryListView.as_view(), name='delivery_list'),
    path('create/', DeliveryCreateView.as_view(), name='new_product'),
    path('deliveries/<int:pk>/', DeliveryDetailView.as_view(), name='delivery_detail'),
    path('deliveries/<int:pk>/update/', DeliveryUpdateView.as_view(), name='delivery_update'),
    path('deliveries/<int:pk>/delete/', DeliveryDeleteView.as_view(), name='delivery_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
]
