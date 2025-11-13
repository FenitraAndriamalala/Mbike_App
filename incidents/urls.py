from django.urls import path
from . import views

urlpatterns = [
    path('', views.incidents_list, name='incidents_list'),
    path('add/', views.incidents_add, name='incidents_add'),
    path('edit/<int:pk>/', views.incidents_edit, name='incidents_edit'),
    path('delete/<int:pk>/', views.incidents_delete, name='incidents_delete'),
]
