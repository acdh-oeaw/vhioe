import django_tables2 as tables
from django_tables2.utils import A
from entries.models import Eintrag, Band


class EintragTable(tables.Table):
    aktenzahl = tables.LinkColumn(
        'entries:eintrag_detail', args=[A('pk')], verbose_name='Akteneintrag')
    band_archiv = tables.Column(accessor='band.archiv', verbose_name="Archiv")
    band = tables.LinkColumn('entities:band_edit', args=[A('pk')], verbose_name='Band')

    class Meta:
        models = Eintrag
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BandTable(tables.Table):
    id = tables.LinkColumn('entities:band_edit', args=[A('pk')], verbose_name='Band')
    archiv = tables.Column(accessor='archiv', verbose_name="Archiv")
    bestand = tables.Column(accessor='bestand', verbose_name="Bestand")
    jahr = tables.Column(accessor='jahr', verbose_name="Jahr")

    class Meta:
        models = Band
        attrs = {"class": "table table-hover table-striped table-condensed"}
