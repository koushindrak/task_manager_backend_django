from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('projects/', views.get_all_projects),
    path('projects/<int:pk>/', views.get_project),
    path('projects/create/', views.create_project),
    path('projects/update/<int:pk>/', views.update_project),
    path('projects/delete/<int:pk>/', views.delete_project),
]
