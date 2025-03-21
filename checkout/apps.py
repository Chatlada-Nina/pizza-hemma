from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the Checkout app.

    This class contains the configuration settings for the checkout app.
    It inherits  from Django's AppConfig and specifies the default
    field type for auto-incrementing fields as BigAutoField.
    The 'name' attribute defines the name of the app.

    Attributes:
    default_auto_field (str): Specifies the default field type for auto fields.
    name (str): The name of the app as a Python path.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # Overiding ready method and import signals module to automatically update orderlinemenu everytime is saved or deleted.
    def ready(self):
        import checkout.signals
        
