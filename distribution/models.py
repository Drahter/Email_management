from django.db import models

from users.models import User


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

    is_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    period = models.CharField(max_length=255, choices=DELIVERY_PERIOD, default='ONCE', verbose_name='периодичность')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='CREATED', verbose_name='статус рассылки')
    is_active = models.BooleanField(default=True, verbose_name='активная рассылка')
    '''Поменять на запрет удаления, уточнить, точно ли удалить'''
    message = models.ForeignKey(Message, on_delete=models.PROTECT, verbose_name='сообщение')
    email_client = models.ManyToManyField(Client, verbose_name='получатели')

    start_delivery = models.DateTimeField(verbose_name='начало рассылки')
    finish_delivery = models.DateTimeField(verbose_name='конец рассылки', blank=True, null=True)
    next_sending = models.DateTimeField(verbose_name='дата следующей рассылки', blank=True, null=True)

    owner = models.ForeignKey(User, verbose_name='автор рассылки', blank=True, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.next_sending = self.start_delivery
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Рассылка №{self.pk}, {self.message}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class SendAttempt(models.Model):
    last_attempt = models.DateTimeField(verbose_name='Дата последней попытки', auto_now_add=True)
    status_attempt = models.BooleanField(verbose_name='Статус', default=False)
    server_answer = models.TextField(max_length=100, blank=True, null=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name='Рассылка', blank=True, null=True)
    client = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'попытка отправки'

    class Meta:
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'
