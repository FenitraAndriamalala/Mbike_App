from django.shortcuts import render, get_object_or_404, redirect
from .models import Incident
from .forms import IncidentForm

def incidents_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incidents/incidents_list.html', {'incidents': incidents})

def incidents_add(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incidents_list')
    else:
        form = IncidentForm()
    return render(request, 'incidents/incidents_form.html', {'form': form})

def incidents_edit(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incidents_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/incidents_form.html', {'form': form})

def incidents_delete(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        incident.delete()
        return redirect('incidents_list')
    return render(request, 'incidents/incidents_confirm_delete.html', {'incident': incident})
