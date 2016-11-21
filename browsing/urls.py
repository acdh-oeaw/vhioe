from django.conf.urls import url
from .views import BrowseEintrag, BrowseBand

urlpatterns = [
    url(r'^browse-entries/$', BrowseEintrag.as_view(), name='browse_entries'),
    url(r'^browse-baende/$', BrowseBand.as_view(), name='browse_baende'),
]
