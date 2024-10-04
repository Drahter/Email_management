import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from distribution.models import Client, SendAttempt, Delivery


def mail_sending(delivery: Delivery, client: Client):
    status_mail = ''
    print(status_mail)
    answer_mail = ''
    print(answer_mail)
    try:
        send_mail(subject=delivery.message.theme,
                  message=delivery.message.content,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[client.email, ]
                  )
        print('delivery.message.theme')
        status_mail = True
        answer_mail = 'Отправлено!'
        print(status_mail)
        print(answer_mail)

    except smtplib.SMTPException as e:
        status_mail = False
        answer_mail = str(e)

    SendAttempt.objects.create(status_attempt=status_mail,
                               server_answer=answer_mail,
                               client=client.email,
                               delivery=delivery
                               )


def my_job():
    print('Проверка готовых к отправке рассылок...')
    zone = pytz.timezone(settings.TIME_ZONE)
    print('1')
    today = datetime.now(zone)
    print('2')
    current_datetime = datetime.now(zone)
    print('3')
    dataset = Delivery.objects.filter(start_delivery__lte=current_datetime).filter(status__in=('CREATED', 'LAUNCHED'))
    print('4')
    for delivery in dataset:
        print('5')
        if delivery.finish_delivery < current_datetime:
            delivery.status = 'COMPLETED'
            print('6')
        else:
            if delivery.status == 'CREATED' and delivery.start_delivery <= current_datetime:
                delivery.status = 'LAUNCHED'
            if today >= delivery.next_sending:
                for client in delivery.email_client.all():
                    mail_sending(delivery, client)
                if delivery.period == 'ONCE':
                    delivery.status = 'COMPLETED'
                elif delivery.period == 'DAILY':
                    delivery.next_sending += timedelta(days=1)
                elif delivery.period == 'WEEKLY':
                    delivery.next_sending += timedelta(days=7)
                elif delivery.period == 'MONTHLY':
                    delivery.next_sending += timedelta(weeks=4)

        delivery.save()
