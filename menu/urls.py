from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_menus, name='all_menus'),
    path('add/', views.add_menu, name='add_menu'),
    path('update/<int:menu_id>/', views.update_menu, name='update_menu'),
    path('delete/<int:menu_id>/', views.delete_menu, name='delete_menu'),
]
