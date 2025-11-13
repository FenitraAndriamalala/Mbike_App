from django.db import models
from velos.models import Velo

class Anomalie(models.Model):
    date = models.DateField()
    nombre_velos = models.IntegerField(default=1)
    velos_utilises = models.ManyToManyField(Velo)
    km_trajet = models.FloatField()
    heure_depart = models.TimeField()
    heure_arrivee = models.TimeField()
    remarque = models.TextField(blank=True)

    def __str__(self):
        return f"Anomalie du {self.date}"
