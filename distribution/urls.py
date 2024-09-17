from django.urls import path
from distribution.apps import DistributionConfig
from distribution.views import MessageListView

app_name = DistributionConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list')
]
