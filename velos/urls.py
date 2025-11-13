from django.urls import path
from . import views

urlpatterns = [
    path('', views.velos_list, name='velos_list'),
    path('add/', views.velos_add, name='velos_add'),
    path('edit/<int:pk>/', views.velos_edit, name='velos_edit'),
    path('delete/<int:pk>/', views.velos_delete, name='velos_delete'),
]
