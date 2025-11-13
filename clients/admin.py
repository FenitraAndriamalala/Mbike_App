from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['numero_client', 'nom', 'prenom', 'mail', 'telephone', 'remarque']
