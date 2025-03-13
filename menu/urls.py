from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_menus, name='all_menus'),
    path('add/', views.add_menu, name='add_menu'),
]
