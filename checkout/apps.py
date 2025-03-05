from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # Overiding ready method and import signals module to automatically update orderlinemenu everytime is saved or deleted.
    def ready(self):
        import checkout.signals
        
