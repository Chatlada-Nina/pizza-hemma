from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_menus, name='all_menus'),
]
