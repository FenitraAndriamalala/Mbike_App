from django.contrib import admin
from .models import Velo

@admin.register(Velo)
class VeloAdmin(admin.ModelAdmin):
    list_display = ['numero', 'type_velo', 'designation', 'taille', 'remarque', 'track', 'demi_journee', 'journee', 'emplacement']
