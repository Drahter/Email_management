from django.apps import AppConfig


class DistributionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'distribution'

    def ready(self):
        from .operator import start
        start()
