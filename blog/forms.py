from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blog.models import Article
from distribution.forms import StyleFormMixin


class ArticleForm(StyleFormMixin, ModelForm):
    """Форма для статей блога"""
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['views_counter', 'is_published', 'created_at', 'slug']

    def clean_title(self):
        """Функции для контроля содержимого статей"""
        cleaned_data = self.cleaned_data.get('title')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такой заголовок недопустим для статьи')

        return cleaned_data

    def clean_content(self):
        """Функции для контроля содержимого статей"""
        cleaned_data = self.cleaned_data.get('content')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for each in forbidden_words:
            if each in cleaned_data:
                raise ValidationError('Извините, такое содержание недопустимо для статьи')

        return cleaned_data
