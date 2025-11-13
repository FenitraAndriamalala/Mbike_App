from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients_list.html', {'clients': clients})

def clients_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm()
    return render(request, 'clients/clients_form.html', {'form': form})

def clients_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/clients_form.html', {'form': form})

def clients_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients_list')
    return render(request, 'clients/clients_confirm_delete.html', {'client': client})
