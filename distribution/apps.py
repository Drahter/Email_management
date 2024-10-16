from django.apps import AppConfig


class DistributionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'distribution'

    def ready(self):
        """Функция для автоматического старта планировщика"""
        from .operator import start
        start()
