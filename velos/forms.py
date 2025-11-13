from django import forms
from .models import Velo

class VeloForm(forms.ModelForm):
    class Meta:
        model = Velo
        fields = '__all__'
