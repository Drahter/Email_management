from django.forms import ModelForm, ValidationError, BooleanField

from distribution.models import Delivery, Message, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class DeliveryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"
        exclude = ['is_created']


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ['theme', 'content']

    def clean_theme(self):
        cleaned_data = self.cleaned_data.get('theme')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такая тема недопустима для сообщения')

        return cleaned_data

    def clean_content(self):
        cleaned_data = self.cleaned_data.get('content')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такое сообщение недопустимо для отправки')

        return cleaned_data


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'comment']
