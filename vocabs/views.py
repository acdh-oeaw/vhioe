from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import SkosConcept, SkosConceptScheme
from .forms import SkosConceptForm, SkosConceptSchemeForm


class SkosConceptDetailView(DetailView):

    model = SkosConcept
    template_name = 'vocabs/skosconcept_detail.html'


class SkosConceptListView(ListView):

    model = SkosConcept
    template_name = 'vocabs/skosconcept_list.html'


class SkosConceptCreate(CreateView):

    model = SkosConcept
    template_name = 'vocabs/skosconcept_create.html'
    form_class = SkosConceptForm


class SkosConceptUpdate(UpdateView):

    model = SkosConcept
    form_class = SkosConceptForm
    template_name = 'vocabs/skosconcept_create.html'


#####################################################
#   ConceptScheme
#####################################################


class SkosConceptSchemeDetailView(DetailView):

    model = SkosConceptScheme
    template_name = 'vocabs/skosconceptscheme_detail.html'


class SkosConceptSchemeListView(ListView):

    model = SkosConceptScheme
    template_name = 'vocabs/skosconceptscheme_list.html'


class SkosConceptSchemeCreate(CreateView):

    model = SkosConceptScheme
    form_class = SkosConceptSchemeForm
    template_name = 'vocabs/skosconcept_create.html'


class SkosConceptSchemeUpdate(UpdateView):

    model = SkosConceptScheme
    form_class = SkosConceptSchemeForm
    template_name = 'vocabs/skosconcept_create.html'
