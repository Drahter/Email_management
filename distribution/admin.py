from django.contrib import admin
from distribution.models import Message, Delivery, Client, SendAttempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Отображение получателей в интерфейсе администратора"""
    list_display = ('full_name', 'email',)
    list_filter = ('full_name',)
    search_fields = ('full_name', 'comment',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    """Отображение рассылок в интерфейсе администратора"""
    list_display = ('is_created', 'period', 'status',)
    list_filter = ('status',)
    search_fields = ('is_created', 'status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Отображение писем в интерфейсе администратора"""
    list_display = ('theme', 'content',)
    search_fields = ('theme', 'content',)


@admin.register(SendAttempt)
class SendAttemptAdmin(admin.ModelAdmin):
    """Отображение попыток отправки в интерфейсе администратора"""
    list_display = ('delivery', 'status_attempt', 'last_attempt',)
    search_fields = ('delivery',)
