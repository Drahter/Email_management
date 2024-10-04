from django.core.management import BaseCommand

from distribution.operator import start


class Command(BaseCommand):
    def handle(self, *args, **options):
        start()
