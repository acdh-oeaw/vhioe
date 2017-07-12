from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Eintrag
from .forms import EintragForm


class EintragDetailView(DetailView):

    model = Eintrag


class EintragListView(ListView):

    model = Eintrag


class EintragCreate(CreateView):

    model = Eintrag
    template_name_suffix = '_create'
    form_class = EintragForm
    success_url = '.'


class EintragUpdate(UpdateView):

    model = Eintrag
    form_class = EintragForm
    template_name_suffix = '_create'
