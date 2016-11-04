from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView
from .forms import *
from .models import EinbringerGechlecht


###########################################################################
# EinbringerGechlecht
###########################################################################


class EinbringerGechlechtListView(generic.ListView):
    model = EinbringerGechlecht
    template_name = 'vocabs/einbringergeschlecht_list_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return EinbringerGechlecht.objects.order_by('name')


def einbringergeschlecht_list_create(request):
    if request.method == "POST":
        form = EinbringerGechlechtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vocabs:einbringergeschlecht_list')
        else:
            return render(request, 'vocabs/einbringergeschlecht_list_create.html', {'form': form})
    else:
        form = EinbringerGechlechtForm()
        return render(request, 'vocabs/einbringergeschlecht_list_create.html', {'form': form})


def einbringergeschlecht_list_edit(request, pk):
    instance = get_object_or_404(EinbringerGechlecht, id=pk)
    if request.method == "POST":
        form = EinbringerGechlechtForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('vocabs:einbringergeschlecht_list')
        else:
            return render(
                request, 'vocabs/einbringergeschlecht_list_create.html',
                {'form': form, 'instance': instance})
    else:
        form = EinbringerGechlechtForm(instance=instance)
        return render(
            request, 'vocabs/einbringergeschlecht_list_create.html',
            {'form': form, 'instance': instance})


class EinbringerGechlechtDelete(DeleteView):
    model = EinbringerGechlecht
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vocabs:einbringergeschlecht_list')


###########################################################################
# Eingangsart
###########################################################################


class EingangsartListView(generic.ListView):
    model = Eingangsart
    template_name = 'vocabs/eingangsart_list_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Eingangsart.objects.order_by('name')


def eingangsart_list_create(request):
    if request.method == "POST":
        form = EingangsartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vocabs:eingangsart_list')
        else:
            return render(request, 'vocabs/eingangsart_list_create.html', {'form': form})
    else:
        form = EingangsartForm()
        return render(request, 'vocabs/eingangsart_list_create.html', {'form': form})


def eingangsart_list_edit(request, pk):
    instance = get_object_or_404(Eingangsart, id=pk)
    if request.method == "POST":
        form = EingangsartForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('vocabs:eingangsart_list')
        else:
            return render(
                request, 'vocabs/eingangsart_list_create.html',
                {'form': form, 'instance': instance})
    else:
        form = EingangsartForm(instance=instance)
        return render(
            request, 'vocabs/eingangsart_list_create.html',
            {'form': form, 'instance': instance})


class EingangsartDelete(DeleteView):
    model = Eingangsart
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vocabs:eingangsart_list')


###########################################################################
# Geschaeftsbereich
###########################################################################


class GeschaeftsbereichListView(generic.ListView):
    model = Geschaeftsbereich
    template_name = 'vocabs/geschaeftsbereich_list_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Geschaeftsbereich.objects.order_by('name')


def geschaeftsbereich_list_create(request):
    if request.method == "POST":
        form = GeschaeftsbereichForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vocabs:geschaeftsbereich_list')
        else:
            return render(request, 'vocabs/geschaeftsbereich_list_create.html', {'form': form})
    else:
        form = GeschaeftsbereichForm()
        return render(request, 'vocabs/geschaeftsbereich_list_create.html', {'form': form})


def geschaeftsbereich_list_edit(request, pk):
    instance = get_object_or_404(Geschaeftsbereich, id=pk)
    if request.method == "POST":
        form = GeschaeftsbereichForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('vocabs:geschaeftsbereich_list')
        else:
            return render(
                request, 'vocabs/geschaeftsbereich_list_create.html',
                {'form': form, 'instance': instance})
    else:
        form = GeschaeftsbereichForm(instance=instance)
        return render(
            request, 'vocabs/geschaeftsbereich_list_create.html',
            {'form': form, 'instance': instance})


class GeschaeftsbereichDelete(DeleteView):
    model = EinbringerGechlecht
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vocabs:geschaeftsbereich_list')


###########################################################################
# Erledigungsart
###########################################################################


class ErledigungsartListView(generic.ListView):
    model = Erledigungsart
    template_name = 'vocabs/erledigungsart_list_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Erledigungsart.objects.order_by('name')


def erledigungsart_list_create(request):
    if request.method == "POST":
        form = ErledigungsartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vocabs:erledigungsart_list')
        else:
            return render(request, 'vocabs/erledigungsart_list_create.html', {'form': form})
    else:
        form = ErledigungsartForm()
        return render(request, 'vocabs/erledigungsart_list_create.html', {'form': form})


def erledigungsart_list_edit(request, pk):
    instance = get_object_or_404(Erledigungsart, id=pk)
    if request.method == "POST":
        form = ErledigungsartForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('vocabs:erledigungsart_list')
        else:
            return render(
                request, 'vocabs/erledigungsart_list_create.html',
                {'form': form, 'instance': instance})
    else:
        form = ErledigungsartForm(instance=instance)
        return render(
            request, 'vocabs/erledigungsart_list_create.html',
            {'form': form, 'instance': instance})


class ErledigungsartDelete(DeleteView):
    model = EinbringerGechlecht
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vocabs:erledigungsart_list')


###########################################################################
# Beruf
###########################################################################


class BerufListView(generic.ListView):
    model = Beruf
    template_name = 'vocabs/beruf_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Beruf.objects.order_by('name')


def beruf_create(request):
    if request.method == "POST":
        form = BerufForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vocabs:beruf_list')
        else:
            return render(request, 'vocabs/beruf_create.html', {'form': form})
    else:
        form = BerufForm()
        return render(request, 'vocabs/beruf_create.html', {'form': form})


def beruf_edit(request, pk):
    instance = get_object_or_404(Beruf, id=pk)
    if request.method == "POST":
        form = BerufForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('vocabs:beruf_list')
        else:
            return render(
                request, 'vocabs/beruf_create.html',
                {'form': form, 'instance': instance})
    else:
        form = BerufForm(instance=instance)
        return render(
            request, 'vocabs/beruf_create.html',
            {'form': form, 'instance': instance})


class BerufDelete(DeleteView):
    model = EinbringerGechlecht
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('vocabs:beruf_list')
