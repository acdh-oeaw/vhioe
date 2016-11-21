from django.conf.urls import url
from . import views
from . import dal_views
from .models import Eintrag


urlpatterns = [
    url(r'^$', views.EintragListView.as_view(), name='eintrag_list'),
    url(r'^(?P<pk>[0-9]+)$', views.EintragDetailView.as_view(), name='eintrag_detail'),
    url(r'^create/$', views.EintragCreate.as_view(), name='eintrag_create'),
    url(r'^update/(?P<pk>[0-9]+)$', views.EintragUpdate.as_view(), name='eintrag_update'),
    url(
        r'^eintrag-autocomplete/$', dal_views.EintragAC.as_view(
            model=Eintrag),
        name='eintrag-autocomplete',
    ),
    # url(r'^delete/(?P<pk>[0-9]+)$', views.PlaceDelete.as_view(), name='place_delete'),
]
