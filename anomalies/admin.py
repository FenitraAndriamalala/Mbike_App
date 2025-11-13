from django.contrib import admin
from .models import Anomalie

@admin.register(Anomalie)
class AnomalieAdmin(admin.ModelAdmin):
    list_display = ['date', 'nombre_velos', 'km_trajet', 'heure_depart', 'heure_arrivee', 'remarque']
