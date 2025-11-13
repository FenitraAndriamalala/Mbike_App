from django.urls import path
from . import views

urlpatterns = [
    path('', views.anomalies_list, name='anomalies_list'),
    path('add/', views.anomalies_add, name='anomalies_add'),
    path('edit/<int:pk>/', views.anomalies_edit, name='anomalies_edit'),
    path('delete/<int:pk>/', views.anomalies_delete, name='anomalies_delete'),
]
