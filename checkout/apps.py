from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    # Line created automatically but does not exist in code along code
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
