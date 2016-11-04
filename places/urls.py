from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.PlaceListView.as_view(), name='place_list'),
    url(r'^create/$', views.create_place, name='place_create'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit_place, name='place_edit'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.PlaceDelete.as_view(), name='place_delete'),
    url(r'^alternativename/list/$', views.AlternativeNameListView.as_view(), name='alternativenames_list'),
    url(r'^alternativename/create/$', views.create_alternativename, name='alternativenames_create'),
    url(r'^alternativename/edit/(?P<pk>[0-9]+)$', views.edit_alternativename, name='alternativenames_edit'),
    url(r'^alternativename/delete/(?P<pk>[0-9]+)$', views.AlternativeNameDelete.as_view(), name='alternativenames_delete')
]
