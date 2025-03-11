from django.db import models
from django.db.models import Sum
from django.conf import settings
from menu.models import MenuItem

# Create your models here.


class Order(models.Model):
    DELIVERY_CHOICES = [
        ('delivery', 'Delivery'),
        ('pickup', 'Pick Up'),
    ]

    order_number = models.AutoField(primary_key=True)
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
    address = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    # clean method ensures the address field is only required if user selects "Delivery"
    def clean(self):
        if self.delivery_method == 'delivery' and not self.address:
            raise ValidationError({'address': 'Address is required for delivery.'})

        
    def update_total(self):
        """
        Check the user's choice of delivery method and update grand total each time a line item is added accounting for delivery costs. 
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
        return str(self.order_number) # Convert order_number to a string.


class OrderLineMenu(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='linemenus')
    menu = models.ForeignKey(MenuItem, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    linemenu_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the linemenu total
        and update the order total.
        """
        self.linemenu_total = self.menu.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.menu.sku} on order {self.order.order_number}'