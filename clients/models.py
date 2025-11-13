from django.db import models

class Client(models.Model):
    numero_client = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.EmailField()
    telephone = models.CharField(max_length=20)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
