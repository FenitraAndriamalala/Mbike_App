from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['date', 'type_incident', 'client', 'service_concerne', 'decouvreur', 'remarque']
