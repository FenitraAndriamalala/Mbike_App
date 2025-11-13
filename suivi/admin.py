from django.contrib import admin
from .models import Suivi

@admin.register(Suivi)
class SuiviAdmin(admin.ModelAdmin):
    list_display = ['velo', 'client', 'semaine_debut', 'semaine_fin', 'parcours', 'ca', 'kms']
