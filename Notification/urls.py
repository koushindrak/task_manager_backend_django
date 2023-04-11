from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.get_all_notifications, name='get_all_notifications'),
    path('notifications/<int:pk>/', views.get_notification, name='get_notification'),
    path('notifications/create/', views.create_notification, name='create_notification'),
    path('notifications/update/<int:pk>/', views.update_notification, name='update_notification'),
    path('notifications/delete/<int:pk>/', views.delete_notification, name='delete_notification'),
]
