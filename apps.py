from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

class CondottieriNotificationConfig(AppConfig):
    name = 'condottieri_notification'
    verbose_name = 'Condottieri Notification'

    def ready(self):
        if not 'pinax.notifications' in settings.INSTALLED_APPS:
            msg = 'You need to include pinax.notifications in INSTALLED_APPS'
            raise ImproperlyConfigured(msg)
