from django.contrib import admin
from .models import Order, OrderLineMenu


class OrderLineMenuAdminInline(admin.TabularInline):
    model = OrderLineMenu
    readonly_fields = ('linemenu_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineMenuAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost',
                       'order_total', 'grand_total', 'original_cart',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email',
              'phone_number', 'delivery_method', 'town_or_city',
              'street_address', 'postcode', 'country', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid',)
    
    list_display = ('order_number', 'date', 'full_name', 'delivery_method',
                    'delivery_cost', 'order_total', 'grand_total',)

    # Ordered by recent order at the top
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
