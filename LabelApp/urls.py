from django.urls import path
from .views import get_all_labels, get_label, create_label, update_label, delete_label

urlpatterns = [
    path('labels/', get_all_labels),
    path('labels/<int:pk>/', get_label),
    path('labels/create/', create_label),
    path('labels/update/<int:pk>/', update_label),
    path('labels/delete/<int:pk>/', delete_label),
]
