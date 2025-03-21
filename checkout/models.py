from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.forms import ValidationError
from menu.models import MenuItem
from profiles.models import UserProfile

# Create your models here.


class Order(models.Model):
    """
    Model representing a customer order in the system.

    This model stores all relevant order details, including the customer's
    personal information, selected delivery method, and the associated items
    in the order.

    **Fields:**
    - `order_number`: A unique auto-generated identifier for the order.
    - `user_profile`: A foreign key linking to the `UserProfile` model.
    - `full_name`: The full name of the customer.
    - `email`: The customer's email address.
    - `phone_number`: The customer's phone number.
    - `delivery_method`: The method of delivery, either 'delivery' or 'pickup'.
    - `country`: The country where the delivery is to be made, default'SE'.
    - `town_or_city`: The town or city for delivery, default 'Gothenburg'.
    - `street_address`: The street address of the customer for delivery.
    - `postcode`: The customer's postal code, optional.
    - `date`: The date and time the order was created.
    - `delivery_cost`: The cost of delivery.
    - `order_total`: The total price of the items, excluding delivery costs.
    - `grand_total`: The total cost of the order, including delivery costs.
    - `original_cart`: A text field storing the original cart data.
    - `stripe_pid`: A reference to the payment identifier used for this order.

    **Methods:**
    - `clean`: Custom validation to ensure that a street address is provided if
    the 'delivery' method is chosen.
    - `update_total`: Updates the order's totals (order total, delivery cost,
    and grand total) whenever line items are added or changed.
    - `__str__`: Returns the order number as a string, providing a
    human-readable representation of the order.

    **Note:**
    - The `delivery_cost` is calculated based on whether the order qualifies
    for free delivery and the chosen delivery method.
    """
    DELIVERY_CHOICES = [
        ('delivery', 'Delivery'),
        ('pickup', 'Pick Up'),
    ]

    order_number = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    delivery_method = models.CharField(
        max_length=10,
        choices=DELIVERY_CHOICES,
        default='delivery',
        null=False,
        blank=False
    )
    country = models.CharField(max_length=40, null=False, blank=False,
                               default='SE')
    town_or_city = models.CharField(max_length=40, null=False, blank=False,
                                    default='Gothenburg')
    street_address = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def clean(self):
        if self.delivery_method == 'delivery' and not self.street_address:
            raise ValidationError({'street_address':
                                  'Street Address is required for delivery.'})

    def update_total(self):
        """
        Check the user's choice of delivery method and update grand total each
        time a line item is added accounting for delivery costs.
        """
        self.order_total = self.linemenus.aggregate(Sum('linemenu_total'))['linemenu_total__sum'] or 0

        if self.delivery_method == 'delivery':
            if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
                self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            else:
                self.delivery_cost = 0
        else:
            self.delivery_cost = 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def __str__(self):
        return str(self.order_number)


class OrderLineMenu(models.Model):
    """
    Represents a line item in an order, associating a menu item with the
    quantity ordered and calculating total cost for that specific line item.

    **Fields:**
    - `order`: A foreign key linking to the `Order` model.
    - `menu`: A foreign key linking to the `MenuItem` model.
    - `quantity`: The number of units of the menu item ordered.
    - `linemenu_total`: The total cost for this line item, calculated as the
    menu item's price multiplied by the quantity ordered.

    **Methods:**
    - `save`: Overrides the default `save` method to calculate the total cost
    of the line item (`linemenu_total`) before saving. It multiplies the
    `menu.price` by the `quantity` to determine the line item’s total.
    - `__str__`: Returns a string representation of the order line, formatted
    as 'SKU {sku} on order {order_number}' for easy identification.

    **Note:**
    - The `linemenu_total` field is automatically computed and cannot be
    directly edited.
    It is updated whenever a change is made to the `quantity` or `menu`.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='linemenus')
    menu = models.ForeignKey(MenuItem, null=False, blank=False,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    linemenu_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the linemenu total
        and update the order total.
        """
        self.linemenu_total = self.menu.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.menu.sku} on order {self.order.order_number}'
