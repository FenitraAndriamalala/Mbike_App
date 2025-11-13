from django.db import models
from clients.models import Client

class Incident(models.Model):
    date = models.DateField()
    type_incident = models.CharField(max_length=200)
    details = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    service_concerne = models.CharField(max_length=200, blank=True)
    decouvreur = models.CharField(max_length=200, blank=True)
    action_interne = models.TextField(blank=True)
    action_client = models.TextField(blank=True)
    procedure_suivre = models.TextField(blank=True)
    action_corrective = models.TextField(blank=True)
    remarque = models.TextField(blank=True)

    def __str__(self):
        return f"Incident du {self.date} - {self.type_incident}"
