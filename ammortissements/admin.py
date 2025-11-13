from django.contrib import admin
from .models import Ammortissement

@admin.register(Ammortissement)
class AmmortissementAdmin(admin.ModelAdmin):
    list_display = ['velo', 'annee', 'prix_neuf', 'kms_total', 'ca_total', 'prix_ca_ammorti', 'decote', 'amortissement_final']
