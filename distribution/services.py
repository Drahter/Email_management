import smtplib

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from distribution.models import Client, SendAttempt, Delivery


def mail_sending(delivery: Delivery, client: Client):
    status_mail = None
    answer_mail = ''
    try:
        send_mail(subject=delivery.message.theme,
                  message=delivery.message.content,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[client.email, ]
                  )
        status_mail = True
        answer_mail = 'Отправлено!'

    except smtplib.SMTPException as e:
        status_mail = False
        answer_mail = str(e)

    SendAttempt.objects.create(status_attempt=status_mail,
                               server_answer=answer_mail,
                               client=client.email,
                               delivery=delivery
                               )
