from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration for the about app.

    THis class contains the configuration settings for the about app.
    It inherits from Django's AppConfig and specifies the default
    field type for auto-incrementing fields ad BigAutoField.
    The 'name' attribute defines the name of the app.

    Attribute:
    default_ayto_field: Specifies the default field type for auto fields.
    name: The name of the app as a Python path.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'

