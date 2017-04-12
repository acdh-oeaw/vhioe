from django.conf.urls import url
from . import views
from .models import Archiv, Institution, Person, Bearbeiter, Band
from places.models import Place
from .import dal_views


urlpatterns = [
    url(r'^person/create/$', views.PersonCreate.as_view(), name='person_create'),
    url(r'^person/edit/(?P<pk>[0-9]+)$', views.PersonUpdate.as_view(), name='person_edit'),
    url(r'^person/delete/(?P<pk>[0-9]+)$', views.PersonDelete.as_view(), name='person_delete'),
    url(r'^person/detail/(?P<pk>[0-9]+)$', views.PersonDetailView.as_view(), name='person_detail'),
    url(r'^band/create/$', views.BandCreate.as_view(), name='band_create'),
    url(r'^band/edit/(?P<pk>[0-9]+)$', views.BandUpdate.as_view(), name='band_edit'),
    url(r'^band/delete/(?P<pk>[0-9]+)$', views.BandDelete.as_view(), name='band_delete'),
    url(r'^band/detail/(?P<pk>[0-9]+)$', views.BandDetailView.as_view(), name='band_detail'),
    url(r'^archiv/create/$', views.ArchivCreate.as_view(), name='archiv_create'),
    url(r'^archiv/edit/(?P<pk>[0-9]+)$', views.ArchivUpdate.as_view(), name='archiv_edit'),
    url(r'^archiv/delete/(?P<pk>[0-9]+)$', views.ArchivDelete.as_view(), name='archiv_delete'),
    url(r'^archiv/detail/(?P<pk>[0-9]+)$', views.ArchivDetailView.as_view(), name='archiv_detail'),
    url(r'^institution/create/$', views.InstitutionCreate.as_view(), name='institution_create'),
    url(
        r'^institution/edit/(?P<pk>[0-9]+)$', views.InstitutionUpdate.as_view(),
        name='institution_edit'),
    url(
        r'^institution/delete/(?P<pk>[0-9]+)$', views.InstitutionDelete.as_view(),
        name='institution_delete'),
    url(
        r'^institution/detail/(?P<pk>[0-9]+)$', views.InstitutionDetailView.as_view(),
        name='institution_detail'),
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
    url(
        r'^ort-autocomplete/$', dal_views.PlaceAC.as_view(
            model=Place,
            create_field='name',),
        name='ort-autocomplete',
    ),
]
