from django.db import models
from cloudinary.models import CloudinaryField


class MenuList(models.Model):
    """
    Represents a category or list of menu items.

    Attributes:
        name (str): The name of the menu list.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Represents an individual menu item.

    Attributes:
        menu_list (ForeignKey): A foreign key to the MenuList model,
            categorizing the menu item.
        sku (str): Stock Keeping Unit, a unique identifier for the item.
        name (str): The name of the menu item.
        description (str): A detailed description of the menu item.
        price (Decimal): The price of the menu item.
        image (CloudinaryField): An image of the menu item, stored on
        Cloudinary.
        created_on (DateField): The date when the menu item was added.
    """

    menu_list = models.ForeignKey(
        'MenuList', null=True, blank=True, on_delete=models.SET_NULL
        )
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
