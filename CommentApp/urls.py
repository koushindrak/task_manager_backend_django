from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_comments, name='get_all_comments'),
    path('<int:pk>/', get_comment, name='get_comment'),
    path('create/', create_comment, name='create_comment'),
    path('update/<int:pk>/', update_comment, name='update_comment'),
    path('delete/<int:pk>/', delete_comment, name='delete_comment'),
]
