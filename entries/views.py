from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EintragCreate, self).dispatch(*args, **kwargs)


class EintragUpdate(UpdateView):

    model = Eintrag
    form_class = EintragForm
    template_name_suffix = '_create'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EintragUpdate, self).dispatch(*args, **kwargs)


class EintragDelete(DeleteView):
    model = Eintrag
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_entries')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EintragDelete, self).dispatch(*args, **kwargs)
