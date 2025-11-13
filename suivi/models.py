from django.db import models
from velos.models import Velo
from clients.models import Client

class Suivi(models.Model):
    velo = models.ForeignKey(Velo, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    semaine_debut = models.DateField()
    semaine_fin = models.DateField()
    parcours = models.CharField(max_length=255, blank=True)
    ca = models.FloatField(default=0)
    kms = models.FloatField(default=0)

    def __str__(self):
        return f"{self.velo} - {self.semaine_debut} à {self.semaine_fin}"
