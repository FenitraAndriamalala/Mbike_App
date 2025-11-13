from django.db import models

class Velo(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    type_velo = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    taille = models.CharField(max_length=20)
    remarque = models.TextField(blank=True, null=True)
    track = models.BooleanField(default=False)
    demi_journee = models.DecimalField(max_digits=8, decimal_places=2)
    journee = models.DecimalField(max_digits=8, decimal_places=2)
    emplacement = models.CharField(max_length=100)
    image = models.ImageField(upload_to='velos_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.numero} - {self.designation}"
