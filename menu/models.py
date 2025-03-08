from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class MenuList(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):

    menu_list = models.ForeignKey('MenuList', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateField(auto_now_add=True)

    # Add a Meta class to define order of items
    class Meta:
        ordering = ["-id"]

    # Display class object as a string to improve readable for admin
    def __str__(self):
        return self.name






