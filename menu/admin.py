from django.contrib import admin
from .models import MenuList, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the MenuItem model.

    This class customizes the Django admin interface for managing menu items,
    providing options for listing, searching, and ordering.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (list): Fields that can be searched in the admin panel.
        ordering (tuple): Default ordering for menu items.
    """
    list_display = (
        'sku',
        'name',
        'menu_list',
        'price',
        'image',
    )
    search_fields = ["name"]
    ordering = ('menu_list',)


@admin.register(MenuList)
class MenuListAdmin(admin.ModelAdmin):
    """
    Admin configuration for the MenuList model.

    This class customizes the Django admin interface for managing menu
    categories.

    Attributes:
        list_display (tuple): Specifies the fields displayed in the admin list
        view.
    """
    list_display = ('name', )
