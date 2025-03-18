from django.db import models

# Create your models here.


class SubscribedUsers(models.Model):

    class Meta:
        verbose_name_plural = 'Subscribed users'

    email = models.EmailField(unique=True, max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # Display class object as a string to improve readable for admin
    def __str__(self):
        return self.email