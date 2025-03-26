from django.db import models


class Contact(models.Model):
    """
    Store a single contact request message.

    This model is used to capture a user's contact information, including their
    name, email, and the message they wish to send. It also includes a `read`
    field to track whether the contact message has been reviewed by the admin.

    Attributes:
        name (str): The full name of the person submitting the contact request.
        email (str): The email address of the person submitting the contact
        request.
        message (str): The message content or inquiry provided by the user.
        read (bool): A flag indicating whether the contact message has been
        read (default is False).

    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact from {self.name}"
