from django.apps import AppConfig


class CartConfig(AppConfig):
    """
    Configuration for the Cart app.

    This class contains the configuration settings for the cart app.
    It inherits  from Django's AppConfig and specifies the default
    field type for auto-incrementing fields as BigAutoField.
    The 'name' attribute defines the name of the app.

    Attributes:
    default_auto_field (str): Specifies the default field type for auto fields.
    name (str): The name of the app as a Python path.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
