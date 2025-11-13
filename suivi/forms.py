from django import forms
from .models import Suivi

class SuiviForm(forms.ModelForm):
    class Meta:
        model = Suivi
        fields = ['velo', 'client', 'semaine_debut', 'semaine_fin', 'parcours', 'ca', 'kms']
