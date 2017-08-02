import django_tables2 as tables
from django_tables2.utils import A
from entries.models import Eintrag, Band, Archiv, Institution, Person, Bearbeiter


class EintragTable(tables.Table):
    aktenzahl = tables.LinkColumn(
        'entries:eintrag_detail', args=[A('pk')], verbose_name='Akteneintrag')
    band_archiv = tables.Column(accessor='band.archiv', verbose_name="Archiv")
    band = tables.LinkColumn(
        'entities:band_detail', accessor='band', args=[A('band.id')],
        verbose_name='Band'
    )

    class Meta:
        models = Eintrag
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BandTable(tables.Table):
    id = tables.LinkColumn('entities:band_detail', args=[A('pk')], verbose_name='Band')
    archiv = tables.Column(accessor='archiv', verbose_name="Archiv")
    bestand = tables.Column(accessor='bestand', verbose_name="Bestand")
    jahr = tables.Column(accessor='jahr', verbose_name="Jahr")

    class Meta:
        models = Band
        attrs = {"class": "table table-hover table-striped table-condensed"}


class ArchivTable(tables.Table):
    name = tables.LinkColumn(
        'entities:archiv_detail', args=[A('pk')], verbose_name='Name')
    akronym = tables.Column(accessor="akronym")
    ort = tables.Column(accessor="ort")
    gnd_id = tables.Column(accessor="gnd_id")

    class Meta:
        models = Archiv
        attrs = {"class": "table table-hover table-striped table-condensed"}


class InstitutionTable(tables.Table):
    name = tables.LinkColumn(
        'entities:institution_detail', args=[A('pk')], verbose_name='Name')
    akronym = tables.Column(accessor="akronym")
    ort = tables.Column(accessor="ort")
    gnd_id = tables.Column(accessor="gnd_id")

    class Meta:
        models = Institution
        attrs = {"class": "table table-hover table-striped table-condensed mytable"}
        #mytable!!!!!!!

    # to remove headers

    def __init__(self, *args, **kwargs):
        super(InstitutionTable, self).__init__(*args, **kwargs)
        self.show_header = False



class PersonTable(tables.Table):
    name = tables.LinkColumn('entities:person_detail', args=[A('pk')], verbose_name='Name ')
    vorname = tables.Column(accessor="vorname")
    sex = tables.Column(accessor="sex")
    beruf = tables.Column(accessor="beruf")
    ort = tables.Column(accessor="ort")
    gnd_id = tables.Column(accessor="gnd_id")

    class Meta:
        models = Person
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BearbeiterTable(tables.Table):
    name = tables.LinkColumn('entities:bearbeiter_detail', args=[A('pk')], verbose_name='Name ')
    vorname = tables.Column(accessor="vorname")
    bearbeiter_kuerzel = tables.Column(accessor="bearbeiter_kuerzel")
    institution = tables.Column(accessor="institution")
    sex = tables.Column(accessor="sex")
    beruf = tables.Column(accessor="beruf")
    ort = tables.Column(accessor="ort")
    gnd_id = tables.Column(accessor="gnd_id")

    class Meta:
        models = Bearbeiter
        attrs = {"class": "table table-hover table-striped table-condensed"}
