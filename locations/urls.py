from django.urls import path
from . import views

urlpatterns = [
    path('', views.locations_list, name='locations_list'),
    path('add/', views.locations_add, name='locations_add'),
    path('edit/<int:pk>/', views.locations_edit, name='locations_edit'),
    path('delete/<int:pk>/', views.locations_delete, name='locations_delete'),
]
