from django.urls import path
from . import views

urlpatterns = [
    path('', views.ammortissements_list, name='ammortissements_list'),
    path('add/', views.ammortissements_add, name='ammortissements_add'),
    path('edit/<int:pk>/', views.ammortissements_edit, name='ammortissements_edit'),
    path('delete/<int:pk>/', views.ammortissements_delete, name='ammortissements_delete'),
]
