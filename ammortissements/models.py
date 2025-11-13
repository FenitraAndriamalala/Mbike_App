from django.db import models
from velos.models import Velo

class Ammortissement(models.Model):
    velo = models.ForeignKey(Velo, on_delete=models.CASCADE)
    annee = models.PositiveIntegerField()
    prix_neuf = models.FloatField()
    kms_total = models.FloatField(default=0)
    ca_total = models.FloatField(default=0)

    def prix_ca_ammorti(self):
        return round(self.ca_total * 0.333, 2)

    def decote(self):
        from datetime import date
        age = date.today().year - self.annee
        if age >= 3:
            return round(self.prix_neuf * 0.80, 2)
        elif age == 2:
            return round(self.prix_neuf * 0.85, 2)
        elif age == 1:
            return round(self.prix_neuf * 0.90, 2)
        else:
            return self.prix_neuf

    def amortissement_final(self):
        return round(self.decote() - self.prix_ca_ammorti(), 2)

    def __str__(self):
        return f"{self.velo} - {self.annee}"
