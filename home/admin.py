from django.contrib import admin
from .models import SubscribedUsers

# Register your models here.


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ("email", "created_on", )


admin.site.register(SubscribedUsers, SubscribedUsersAdmin)