from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<menu_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<menu_id>/', views.update_cart, name='update_cart'),
    path('remove/<menu_id>/', views.remove_from_cart, name='remove_from_cart'),
]
