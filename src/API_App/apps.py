from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    name = 'API_App'

    def ready(self, *args, **kwargs):
        import API_App.signals
