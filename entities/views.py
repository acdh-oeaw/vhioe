from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import BandForm, ArchivForm, InstitutionForm, PersonForm
from .models import Band, Archiv, Institution, Person


class PersonListView(generic.ListView):
    model = Person
    template_name = 'entities/band_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Person.objects.order_by('signatur')


class PersonDetailView(DetailView):

    model = Person


class PersonCreate(CreateView):

    model = Person
    template_name_suffix = '_create'
    form_class = PersonForm


class PersonUpdate(UpdateView):

    model = Person
    template_name_suffix = '_create'
    form_class = PersonForm


class PersonDelete(DeleteView):
    model = Person
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_persons')


class BandListView(generic.ListView):
    model = Band
    template_name = 'entities/band_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Band.objects.order_by('signatur')


class BandDetailView(DetailView):

    model = Band


class BandCreate(CreateView):

    model = Band
    template_name_suffix = '_create'
    form_class = BandForm


class BandUpdate(UpdateView):

    model = Band
    template_name_suffix = '_create'
    form_class = BandForm


class BandDelete(DeleteView):
    model = Band
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_baende')


# Archiv


class ArchivDetailView(DetailView):

    model = Archiv


class ArchivCreate(CreateView):

    model = Archiv
    template_name_suffix = '_create'
    form_class = ArchivForm


class ArchivUpdate(UpdateView):

    model = Archiv
    template_name_suffix = '_create'
    form_class = ArchivForm


class ArchivDelete(DeleteView):
    model = Archiv
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_archivs')


# Institution


class InstitutionDetailView(DetailView):

    model = Institution


class InstitutionCreate(CreateView):

    model = Institution
    template_name_suffix = '_create'
    form_class = InstitutionForm


class InstitutionUpdate(UpdateView):

    model = Institution
    template_name_suffix = '_create'
    form_class = InstitutionForm


class InstitutionDelete(DeleteView):
    model = Institution
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browse_institutions')
