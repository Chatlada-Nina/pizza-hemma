from django.contrib import admin
from .models import MenuList, MenuItem

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
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
    list_display = ('name', )
