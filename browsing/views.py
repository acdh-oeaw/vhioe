from django_tables2 import SingleTableView, RequestConfig
from .filters import *
from .forms import GenericFilterFormHelper
from .tables import *
from entries.models import Eintrag, Band, Archiv, Institution, Person, Bearbeiter


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class BrowseEintrag(GenericListView):
    model = Eintrag
    table_class = EintragTable
    template_name = 'browsing/eintrag_list_generic.html'
    filter_class = EintragListFilter
    formhelper_class = GenericFilterFormHelper


class BrowseBand(GenericListView):
    model = Band
    table_class = BandTable
    template_name = 'browsing/band_list_generic.html'
    filter_class = BandListFilter
    formhelper_class = GenericFilterFormHelper


class BrowseArchiv(GenericListView):
    model = Archiv
    table_class = ArchivTable
    template_name = 'browsing/archiv_list_generic.html'
    filter_class = ArchivListFilter
    formhelper_class = GenericFilterFormHelper


class BrowseInstitution(GenericListView):
    model = Institution
    table_class = InstitutionTable
    template_name = 'browsing/institution_list_generic.html'
    filter_class = InstitutionListFilter
    formhelper_class = GenericFilterFormHelper


class BrowsePerson(GenericListView):
    model = Person
    table_class = PersonTable
    template_name = 'browsing/person_list_generic.html'
    filter_class = PersonListFilter
    formhelper_class = GenericFilterFormHelper


class BrowseBearbeiter(GenericListView):
    model = Bearbeiter
    table_class = BearbeiterTable
    template_name = 'browsing/bearbeiter_list_generic.html'
    filter_class = BearbeiterListFilter
    formhelper_class = GenericFilterFormHelper
