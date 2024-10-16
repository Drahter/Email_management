import smtplib
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache import cache

from blog.models import Article
from config.settings import EMAIL_HOST_USER, CACHE_ENABLED
from distribution.models import Client, SendAttempt, Delivery


def mail_sending(delivery: Delivery, client: Client):
    """Функция для отправки писем и формирования ответа сервиса рассылки"""
    try:
        send_mail(subject=delivery.message.theme,
                  message=delivery.message.content,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[client.email, ],
                  )
        status_mail = True
        answer_mail = 'Отправлено!'
    except smtplib.SMTPException as e:
        status_mail = False
        answer_mail = str(e)

    """fail silently, что возвращает сенд маил"""
    """Формирует объект попытки отправки для логов"""
    SendAttempt.objects.create(status_attempt=status_mail,
                               server_answer=answer_mail,
                               client=client.email,
                               delivery=delivery
                               )


def my_job():
    """
    Основная функция для планировщика, проверяет все рассылки по времени начала и дате следующей отправки,
    при соответствии условий отсылает письмо и меняет дату следующей отправки
    """
    print('Проверка готовых к отправке рассылок...')
    zone = pytz.timezone(settings.TIME_ZONE)

    current_datetime = datetime.now(zone)

    dataset = Delivery.objects.filter(
        start_delivery__lte=current_datetime,
        status__in=('CREATED', 'LAUNCHED')
    )

    for delivery in dataset:

        if delivery.finish_delivery < current_datetime:
            delivery.status = 'COMPLETED'

        else:
            if delivery.status == 'CREATED' and delivery.start_delivery <= current_datetime:
                delivery.status = 'LAUNCHED'
            if current_datetime >= delivery.next_sending and delivery.is_active:
                for client in delivery.email_client.all():
                    mail_sending(delivery, client)
                if delivery.period == 'ONCE':
                    delivery.status = 'COMPLETED'
                elif delivery.period == 'DAILY':
                    delivery.next_sending += timedelta(days=1)
                elif delivery.period == 'WEEKLY':
                    delivery.next_sending += timedelta(days=7)
                elif delivery.period == 'MONTHLY':
                    delivery.next_sending += relativedelta(months=1)

        delivery.save()


def get_articles_from_cache():
    """Функция для кэширования статей блога"""
    if not CACHE_ENABLED:
        return Article.objects.all()
    key = "articles_list"
    articles = cache.get(key)
    if articles is not None:
        return articles

    articles = Article.objects.all()
    cache.set(key, articles)
    return articles
