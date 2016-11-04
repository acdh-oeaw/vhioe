from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^baende/$', views.BandListView.as_view(), name='baende_list'),
    url(r'^band/create/$', views.band_create, name='band_create'),
    url(r'^band/edit/(?P<pk>[0-9]+)$', views.band_edit, name='band_edit'),
    url(r'^band/delete/(?P<pk>[0-9]+)$', views.BandDelete.as_view(), name='band_delete'),
]
