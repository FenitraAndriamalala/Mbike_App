from django.urls import path
from . import views

urlpatterns = [
    path('', views.suivi_list, name='suivi_list'),
    path('add/', views.suivi_add, name='suivi_add'),
    path('edit/<int:pk>/', views.suivi_edit, name='suivi_edit'),
    path('delete/<int:pk>/', views.suivi_delete, name='suivi_delete'),
]
