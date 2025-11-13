from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['date', 'type_incident', 'details', 'client', 'service_concerne',
                  'decouvreur', 'action_interne', 'action_client', 'procedure_suivre',
                  'action_corrective', 'remarque']
