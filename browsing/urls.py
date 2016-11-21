from django.conf.urls import url
from .views import BrowseEintrag

urlpatterns = [
    url(r'^browse-entries/$', BrowseEintrag.as_view(), name='browse_entries'),
]
