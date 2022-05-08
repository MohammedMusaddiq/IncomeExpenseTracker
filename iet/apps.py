from django.apps import AppConfig


class IetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iet'

    def ready(self):
        pass
