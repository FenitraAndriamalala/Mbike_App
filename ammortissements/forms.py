from django import forms
from .models import Ammortissement

class AmmortissementForm(forms.ModelForm):
    class Meta:
        model = Ammortissement
        fields = ['velo', 'annee', 'prix_neuf', 'kms_total', 'ca_total']
