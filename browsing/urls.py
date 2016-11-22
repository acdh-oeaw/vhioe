from django.conf.urls import url
from .views import BrowseEintrag, BrowseBand, BrowseArchiv, BrowseInstitution, BrowsePerson

urlpatterns = [
    url(r'^browse-entries/$', BrowseEintrag.as_view(), name='browse_entries'),
    url(r'^browse-baende/$', BrowseBand.as_view(), name='browse_baende'),
    url(r'^browse-archivs/$', BrowseArchiv.as_view(), name='browse_archivs'),
    url(r'^browse-institutions/$', BrowseInstitution.as_view(), name='browse_institutions'),
    url(r'^browse-persons/$', BrowsePerson.as_view(), name='browse_persons'),
    url(r'^browse-bearbeiter/$', BrowsePerson.as_view(), name='browse_bearbeiter'),
]
