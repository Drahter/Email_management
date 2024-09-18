from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='имя получателя')
    email = models.EmailField(verbose_name='электронная почта')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'


class Message(models.Model):
    theme = models.CharField(max_length=100, verbose_name='тема сообщения')
    content = models.TextField(verbose_name='содержание сообщения')

    def __str__(self):
        return f'Тема: {self.theme}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Delivery(models.Model):
    STATUS_CHOICES = (
        ('CREATED', 'создана'),
        ('LAUNCHED', 'запущена'),
        ('COMPLETED', 'завершена'),
    )
    DELIVERY_PERIOD = (
        ('ONCE', 'однократно'),
        ('DAILY', 'ежедневно'),
        ('WEEKLY', 'еженедельно'),
        ('MONTHLY', 'ежемесячно'),
    )

    is_created = models.DateTimeField(auto_now_add=True, verbose_name='первая отправка')
    period = models.CharField(max_length=255, choices=DELIVERY_PERIOD, default='ONCE', verbose_name='периодичность')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='CREATED', verbose_name='статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='активная рассылка')
    email_client = models.ManyToManyField(Client, verbose_name='получатели')

    def __str__(self):
        return f'Рассылка № {self.pk} от {self.is_created}, периодичность:  {self.period}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class SendTry(models.Model):
    pass
