from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^beruf/$', views.BerufListView.as_view(), name='beruf_list'),
    url(r'^beruf/create/$', views.beruf_create, name='beruf_create'),
    url(r'^beruf/edit/(?P<pk>[0-9]+)$', views.beruf_edit, name='beruf_edit'),
    url(r'^beruf/delete/(?P<pk>[0-9]+)$', views.BerufDelete.as_view(), name='beruf_delete'),
]
