import django_tables2 as tables
from django_tables2.utils import A
from entries.models import Eintrag


class EintragTable(tables.Table):
    band_archiv = tables.Column(accessor='band.archiv', verbose_name="Archiv")
    band = tables.LinkColumn('entities:band_edit', args=[A('pk')], verbose_name='Band')
    aktenzahl = tables.LinkColumn(
        'entries:eintrag_detail', args=[A('pk')], verbose_name='Akteneintrag')

    class Meta:
        models = Eintrag
        attrs = {"class": "table table-hover table-striped table-condensed"}
