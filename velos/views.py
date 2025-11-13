from django.shortcuts import render, get_object_or_404, redirect
from .models import Velo
from .forms import VeloForm

def velos_list(request):
    velos = Velo.objects.all()
    return render(request, 'velos/velos_list.html', {'velos': velos})

def velos_add(request):
    if request.method == 'POST':
        form = VeloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('velos_list')
    else:
        form = VeloForm()
    return render(request, 'velos/velos_form.html', {'form': form})

def velos_edit(request, pk):
    velo = get_object_or_404(Velo, pk=pk)
    if request.method == 'POST':
        form = VeloForm(request.POST, request.FILES, instance=velo)
        if form.is_valid():
            form.save()
            return redirect('velos_list')
    else:
        form = VeloForm(instance=velo)
    return render(request, 'velos/velos_form.html', {'form': form})

def velos_delete(request, pk):
    velo = get_object_or_404(Velo, pk=pk)
    if request.method == 'POST':
        velo.delete()
        return redirect('velos_list')
    return render(request, 'velos/velos_confirm_delete.html', {'velo': velo})
