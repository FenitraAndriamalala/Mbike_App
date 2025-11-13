from django import forms
from .models import Anomalie

class AnomalieForm(forms.ModelForm):
    class Meta:
        model = Anomalie
        fields = ['date', 'nombre_velos', 'velos_utilises', 'km_trajet', 'heure_depart', 'heure_arrivee', 'remarque']
