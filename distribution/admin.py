from django.contrib import admin
from distribution.models import Message, Delivery, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',)
    list_filter = ('full_name', )
    search_fields = ('full_name', 'comment',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('is_created', 'period', 'status',)
    list_filter = ('status', )
    search_fields = ('is_created', 'status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'content',)
    search_fields = ('theme', 'content',)
