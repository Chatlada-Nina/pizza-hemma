from django.urls import path
from . import views


urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('review_edit/<int:review_id>', views.review_edit, name='review_edit'),
]