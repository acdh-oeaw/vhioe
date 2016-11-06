from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SkosConceptListView.as_view(), name='skosconcept_list'),
    url(r'^(?P<pk>[0-9]+)$', views.SkosConceptDetailView.as_view(), name='skosconcept_detail'),
    url(r'^create/$', views.SkosConceptCreate.as_view(), name='skosconcept_create'),
    url(r'^update/(?P<pk>[0-9]+)$', views.SkosConceptUpdate.as_view(), name='skosconcept_update'),
    # url(r'^delete/(?P<pk>[0-9]+)$', views.PlaceDelete.as_view(), name='place_delete'),
]
