from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from distribution.models import Message, Client


def mail_sending(message: Message, client: Client):
    send_mail(
        message.theme,
        message.content,
        EMAIL_HOST_USER,
        [client.email],
    )
