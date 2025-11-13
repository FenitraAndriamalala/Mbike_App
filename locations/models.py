from django.db import models
from clients.models import Client
from velos.models import Velo


class Location(models.Model):
    TYPE_LOCATION_CHOICES = [
        ('1/2 journée', '1/2 journée'),
        ('1 journée', '1 journée'),
    ]

    date = models.DateField()
    type_location = models.CharField(max_length=20, choices=TYPE_LOCATION_CHOICES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nombre_participants = models.PositiveIntegerField()
    velo = models.ForeignKey(Velo, on_delete=models.CASCADE)
    taille = models.CharField(max_length=20)
    circuit_prevu = models.CharField(max_length=255, blank=True, null=True)
    localisation_velo = models.CharField(max_length=255, blank=True, null=True)
    remarque = models.TextField(blank=True, null=True)
    clef = models.CharField(max_length=50, blank=True, null=True)
    km_trajet = models.FloatField(blank=True, null=True)
    guide = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.client} - {self.date} - {self.type_location}"
