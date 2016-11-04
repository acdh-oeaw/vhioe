from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView
from .forms import BandForm
from .models import Band


class BandListView(generic.ListView):
    model = Band
    template_name = 'entities/band_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Band.objects.order_by('signatur')


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entities:baende_list')
        else:
            return render(request, 'entities/band_create.html', {'form': form})
    else:
        form = BandForm()
        return render(request, 'entities/band_create.html', {'form': form})


def band_edit(request, pk):
    instance = get_object_or_404(Band, id=pk)
    if request.method == "POST":
        form = BandForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('entities:baende_list')
        else:
            return render(request, 'entities/band_create.html', {'form': form, 'instance': instance})
    else:
        form = BandForm(instance=instance)
        return render(request, 'entities/band_create.html', {'form': form, 'instance': instance})


class BandDelete(DeleteView):
    model = Band
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:baende_list')
