from django.urls import path
from .views import signup
from . import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:id>/', views.user_detail, name='user-detail'),
    path('users/update/<int:id>/', views.user_update, name='user-update'),
    path('users/delete/<int:id>/', views.user_delete, name='user-delete'),
    path('teams/<int:team_id>/users/', views.user_list_by_team, name='user-list-by-team'),

]