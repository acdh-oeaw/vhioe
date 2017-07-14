from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import BandForm, ArchivForm, InstitutionForm, PersonForm, BearbeiterForm
from .models import Band, Archiv, Institution, Person, Bearbeiter


class BearbeiterListView(generic.ListView):
    model = Bearbeiter
    template_name = 'entities/bearbeiter_list.html'
    context_object_name = 'object_list'


class BearbeiterDetailView(DetailView):

    model = Bearbeiter


class BearbeiterCreate(CreateView):

    model = Bearbeiter
    template_name_suffix = '_create'
    form_class = BearbeiterForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BearbeiterCreate, self).dispatch(*args, **kwargs)


class BearbeiterUpdate(UpdateView):

    model = Bearbeiter
    template_name_suffix = '_create'
    form_class = BearbeiterForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BearbeiterUpdate, self).dispatch(*args, **kwargs)


class BearbeiterDelete(DeleteView):
    model = Bearbeiter
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_bearbeiter')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BearbeiterDelete, self).dispatch(*args, **kwargs)


class PersonListView(generic.ListView):
    model = Person
    template_name = 'entities/band_list.html'
    context_object_name = 'object_list'


class PersonDetailView(DetailView):

    model = Person


class PersonCreate(CreateView):

    model = Person
    template_name_suffix = '_create'
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(UpdateView):

    model = Person
    template_name_suffix = '_create'
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)


class PersonDelete(DeleteView):
    model = Person
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_persons')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BandCreate, self).dispatch(*args, **kwargs)


class BandUpdate(UpdateView):

    model = Band
    template_name_suffix = '_create'
    form_class = BandForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BandUpdate, self).dispatch(*args, **kwargs)


class BandDelete(DeleteView):
    model = Band
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_baende')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BandDelete, self).dispatch(*args, **kwargs)


# Archiv


class ArchivDetailView(DetailView):

    model = Archiv


class ArchivCreate(CreateView):

    model = Archiv
    template_name_suffix = '_create'
    form_class = ArchivForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArchivCreate, self).dispatch(*args, **kwargs)


class ArchivUpdate(UpdateView):

    model = Archiv
    template_name_suffix = '_create'
    form_class = ArchivForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArchivUpdate, self).dispatch(*args, **kwargs)


class ArchivDelete(DeleteView):
    model = Archiv
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_archivs')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArchivDelete, self).dispatch(*args, **kwargs)


# Institution


class InstitutionDetailView(DetailView):

    model = Institution


class InstitutionCreate(CreateView):

    model = Institution
    template_name_suffix = '_create'
    form_class = InstitutionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionDelete, self).dispatch(*args, **kwargs)


class InstitutionUpdate(UpdateView):

    model = Institution
    template_name_suffix = '_create'
    form_class = InstitutionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionUpdate, self).dispatch(*args, **kwargs)


class InstitutionDelete(DeleteView):
    model = Institution
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_institutions')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionDelete, self).dispatch(*args, **kwargs)
