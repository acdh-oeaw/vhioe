from django.conf.urls import url
from . import views
from . import dal_views
from .models import SkosLabel

urlpatterns = [
    url(r'^$', views.SkosConceptListView.as_view(), name='skosconcept_list'),
    url(r'^(?P<pk>[0-9]+)$', views.SkosConceptDetailView.as_view(), name='skosconcept_detail'),
    url(r'^create/$', views.SkosConceptCreate.as_view(), name='skosconcept_create'),
    url(r'^update/(?P<pk>[0-9]+)$', views.SkosConceptUpdate.as_view(), name='skosconcept_update'),
    # url(r'^delete/(?P<pk>[0-9]+)$', views.PlaceDelete.as_view(), name='place_delete'),
    url(r'^scheme/$', views.SkosConceptSchemeListView.as_view(), name='skosconceptscheme_list'),
    url(
        r'^scheme/(?P<pk>[0-9]+)$', views.SkosConceptSchemeDetailView.as_view(),
        name='skosconceptscheme_detail'),
    url(
        r'^scheme/create/$', views.SkosConceptSchemeCreate.as_view(),
        name='skosconceptscheme_create'),
    url(
        r'^scheme/update/(?P<pk>[0-9]+)$', views.SkosConceptSchemeUpdate.as_view(),
        name='skosconceptscheme_update'),
    url(r'^label/$', views.SkosLabelListView.as_view(), name='skoslabel_list'),
    url(
        r'^label/(?P<pk>[0-9]+)$', views.SkosLabelDetailView.as_view(),
        name='skoslabel_detail'),
    url(
        r'^label/create/$', views.SkosLabelCreate.as_view(),
        name='skoslabel_create'),
    url(
        r'^label/update/(?P<pk>[0-9]+)$', views.SkosLabelUpdate.as_view(),
        name='skoslabel_update'),
    url(
        r'^skoslabel-autocomplete/$', dal_views.SkosLabelAC.as_view(model=SkosLabel,
            create_field='label',),
        name='skoslabel-autocomplete',
    ),
]
