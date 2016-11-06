from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import SkosConcept


class SkosConceptDetailView(DetailView):

    model = SkosConcept


class SkosConceptListView(ListView):

    model = SkosConcept


class SkosConceptCreate(CreateView):

    model = SkosConcept
    fields = "__all__"
    template_name_suffix = '_create'


class SkosConceptUpdate(UpdateView):

    model = SkosConcept
    fields = "__all__"

    template_name_suffix = '_create'
