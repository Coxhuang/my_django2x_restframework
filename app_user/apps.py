from django.apps import AppConfig


class AppUserConfig(AppConfig):
    name = 'app_user'

    def ready(self):
        import utils.common.signals.signal # signal.py路径
