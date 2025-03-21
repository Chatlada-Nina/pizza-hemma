from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    Configuration class for the 'contact' application.

    This class is used by Django to configure settings for the Contact app,
    including specifying the default primary key field type and the app name.

    Attributes:
        default_auto_field:
        The field type used for auto-incrementing primary keys.
        name: The name of the application within the project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
