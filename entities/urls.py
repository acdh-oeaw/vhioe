from django.conf.urls import url
from . import views
from .models import Archiv, Institution, Person, Bearbeiter, Band
from .import dal_views


urlpatterns = [
    url(r'^baende/$', views.BandListView.as_view(), name='baende_list'),
    url(r'^band/create/$', views.band_create, name='band_create'),
    url(r'^band/edit/(?P<pk>[0-9]+)$', views.band_edit, name='band_edit'),
    url(r'^band/delete/(?P<pk>[0-9]+)$', views.BandDelete.as_view(), name='band_delete'),
    url(
        r'^archiv-autocomplete/$', dal_views.ArchivAC.as_view(
            model=Archiv,
            create_field='name',),
        name='archiv-autocomplete',
    ),
    url(
        r'^institution-autocomplete/$', dal_views.InstitutionAC.as_view(
            model=Institution,
            create_field='name',),
        name='institution-autocomplete',
    ),
    url(
        r'^person-autocomplete/$', dal_views.PersonAC.as_view(
            model=Person,
            create_field='name',),
        name='person-autocomplete',
    ),
    url(
        r'^bearbeiter-autocomplete/$', dal_views.BearbeiterAC.as_view(
            model=Bearbeiter,
            create_field='name',),
        name='bearbeiter-autocomplete',
    ),
    url(
        r'^band-autocomplete/$', dal_views.BandAC.as_view(
            model=Band,
            create_field='name',),
        name='band-autocomplete',
    ),
]
