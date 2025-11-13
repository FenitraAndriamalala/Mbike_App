from django.shortcuts import render, get_object_or_404, redirect
from .models import Anomalie
from .forms import AnomalieForm

def anomalies_list(request):
    anomalies = Anomalie.objects.all()
    return render(request, 'anomalies/anomalies_list.html', {'anomalies': anomalies})

def anomalies_add(request):
    if request.method == 'POST':
        form = AnomalieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anomalies_list')
    else:
        form = AnomalieForm()
    return render(request, 'anomalies/anomalies_form.html', {'form': form})

def anomalies_edit(request, pk):
    anomalie = get_object_or_404(Anomalie, pk=pk)
    if request.method == 'POST':
        form = AnomalieForm(request.POST, instance=anomalie)
        if form.is_valid():
            form.save()
            return redirect('anomalies_list')
    else:
        form = AnomalieForm(instance=anomalie)
    return render(request, 'anomalies/anomalies_form.html', {'form': form})

def anomalies_delete(request, pk):
    anomalie = get_object_or_404(Anomalie, pk=pk)
    if request.method == 'POST':
        anomalie.delete()
        return redirect('anomalies_list')
    return render(request, 'anomalies/anomalies_confirm_delete.html', {'anomalie': anomalie})
