from django.db import models


class About(models.Model):
    """
    This model stores details that will be displayed on
    the about page of the website.
    It includes fields 'title' and 'content'
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    # Display class object as a string to improve readable for admin
    def __str__(self):
        return self.title
