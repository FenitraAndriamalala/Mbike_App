from django.shortcuts import render, get_object_or_404, redirect
from .models import Location
from .forms import LocationForm

def locations_list(request):
    locations = Location.objects.all()
    return render(request, 'locations/locations_list.html', {'locations': locations})

def locations_add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations_list')
    else:
        form = LocationForm()
    return render(request, 'locations/locations_form.html', {'form': form})

def locations_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('locations_list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'locations/locations_form.html', {'form': form})

def locations_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('locations_list')
    return render(request, 'locations/locations_confirm_delete.html', {'location': location})
