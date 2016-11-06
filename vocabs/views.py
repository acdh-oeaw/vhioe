from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import SkosConcept
from .forms import SkosConceptForm


class SkosConceptDetailView(DetailView):

    model = SkosConcept


class SkosConceptListView(ListView):

    model = SkosConcept


class SkosConceptCreate(CreateView):

    model = SkosConcept
    template_name_suffix = '_create'
    form_class = SkosConceptForm


class SkosConceptUpdate(UpdateView):

    model = SkosConcept
    form_class = SkosConceptForm
    template_name_suffix = '_create'
