from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['date', 'type_location', 'client', 'nombre_participants',
                    'velo', 'taille', 'circuit_prevu', 'localisation_velo',
                    'remarque', 'clef', 'km_trajet', 'guide']
