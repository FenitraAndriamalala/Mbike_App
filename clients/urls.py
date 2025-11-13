from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('add/', views.clients_add, name='clients_add'),
    path('edit/<int:pk>/', views.clients_edit, name='clients_edit'),
    path('delete/<int:pk>/', views.clients_delete, name='clients_delete'),
]
