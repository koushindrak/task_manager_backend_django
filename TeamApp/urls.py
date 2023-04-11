from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.get_all_teams, name='get_all_teams'),
    path('teams/<int:pk>/', views.get_team, name='get_team'),
    path('teams/create/', views.create_team, name='create_team'),
    path('teams/update/<int:pk>/', views.update_team, name='update_team'),
    path('teams/delete/<int:pk>/', views.delete_team, name='delete_team'),
]
