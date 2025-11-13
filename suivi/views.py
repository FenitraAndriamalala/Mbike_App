from django.shortcuts import render, get_object_or_404, redirect
from .models import Suivi
from .forms import SuiviForm

def suivi_list(request):
    suivis = Suivi.objects.all()
    return render(request, 'suivi/suivi_list.html', {'suivis': suivis})

def suivi_add(request):
    if request.method == 'POST':
        form = SuiviForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suivi_list')
    else:
        form = SuiviForm()
    return render(request, 'suivi/suivi_form.html', {'form': form})

def suivi_edit(request, pk):
    suivi = get_object_or_404(Suivi, pk=pk)
    if request.method == 'POST':
        form = SuiviForm(request.POST, instance=suivi)
        if form.is_valid():
            form.save()
            return redirect('suivi_list')
    else:
        form = SuiviForm(instance=suivi)
    return render(request, 'suivi/suivi_form.html', {'form': form})

def suivi_delete(request, pk):
    suivi = get_object_or_404(Suivi, pk=pk)
    if request.method == 'POST':
        suivi.delete()
        return redirect('suivi_list')
    return render(request, 'suivi/suivi_confirm_delete.html', {'suivi': suivi})
