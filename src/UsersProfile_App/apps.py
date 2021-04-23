from django.apps import AppConfig


class UsersprofileAppConfig(AppConfig):
    name = 'UsersProfile_App'

    def ready(self, *args, **kwargs):
        import UsersProfile_App.signals
