from django.core.management import BaseCommand

from distribution.operator import start


class Command(BaseCommand):
    help = 'Start APscheduler'

    def handle(self, *args, **options):
        s = start()
        return s
