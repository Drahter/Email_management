from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='имя клиента')
    email = models.EmailField(verbose_name='электронная почта')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Delivery(models.Model):
    is_created = models.DateTimeField(auto_now_add=True, verbose_name='первая отправка')
    period = models.PositiveIntegerField(verbose_name='периодичность')
    status = models.CharField(max_length=100, verbose_name='статус рассылки')

    def __str__(self):
        return f'Отправлено {self.is_created}, повтор каждые {self.period} дн.'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    theme = models.CharField(max_length=100, verbose_name='тема сообщения')
    content = models.TextField(verbose_name='содержание сообщения')

    def __str__(self):
        return f'Тема: {self.theme}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class SendTry(models.Model):
    pass
