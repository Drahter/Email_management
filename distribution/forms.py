from django import forms
from django.forms import ModelForm, ValidationError, BooleanField

from distribution.models import Delivery, Message, Client


class StyleFormMixin:
    """Миксин для стандартизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

            if isinstance(field.widget, forms.widgets.DateTimeInput):
                field.widget.input_type = 'datetime-local'


class DeliveryForm(StyleFormMixin, ModelForm):
    """Форма для рассылок"""
    class Meta:
        model = Delivery
        fields = "__all__"
        exclude = ['is_created', 'next_sending', 'owner']


class MessageForm(StyleFormMixin, ModelForm):
    """Форма для писем"""
    class Meta:
        model = Message
        fields = ['theme', 'content']

    def clean_theme(self):
        """Функции для контроля содержимого писем"""
        cleaned_data = self.cleaned_data.get('theme')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такая тема недопустима для сообщения')

        return cleaned_data

    def clean_content(self):
        """Функции для контроля содержимого писем"""
        cleaned_data = self.cleaned_data.get('content')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такое сообщение недопустимо для отправки')

        return cleaned_data


class ClientForm(StyleFormMixin, ModelForm):
    """Форма для получателей"""
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'comment']
