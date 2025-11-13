from django.shortcuts import render, get_object_or_404, redirect
from .models import Ammortissement
from .forms import AmmortissementForm

def ammortissements_list(request):
    ammortissements = Ammortissement.objects.all()
    return render(request, 'ammortissements/ammortissements_list.html', {'ammortissements': ammortissements})

def ammortissements_add(request):
    if request.method == 'POST':
        form = AmmortissementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ammortissements_list')
    else:
        form = AmmortissementForm()
    return render(request, 'ammortissements/ammortissements_form.html', {'form': form})

def ammortissements_edit(request, pk):
    ammortissement = get_object_or_404(Ammortissement, pk=pk)
    if request.method == 'POST':
        form = AmmortissementForm(request.POST, instance=ammortissement)
        if form.is_valid():
            form.save()
            return redirect('ammortissements_list')
    else:
        form = AmmortissementForm(instance=ammortissement)
    return render(request, 'ammortissements/ammortissements_form.html', {'form': form})

def ammortissements_delete(request, pk):
    ammortissement = get_object_or_404(Ammortissement, pk=pk)
    if request.method == 'POST':
        ammortissement.delete()
        return redirect('ammortissements_list')
    return render(request, 'ammortissements/ammortissements_confirm_delete.html', {'ammortissement': ammortissement})
