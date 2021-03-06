import django_filters
from entries.models import Eintrag, Band, Archiv, Institution, Person, Bearbeiter


django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class EintragListFilter(django_filters.FilterSet):

    class Meta:
        model = Eintrag
        fields = ['band']


class BandListFilter(django_filters.FilterSet):

    class Meta:
        model = Band
        fields = "__all__"


class ArchivListFilter(django_filters.FilterSet):

    class Meta:
        model = Archiv
        fields = "__all__"


class InstitutionListFilter(django_filters.FilterSet):

    class Meta:
        model = Institution
        fields = "__all__"


class PersonListFilter(django_filters.FilterSet):

    class Meta:
        model = Person
        fields = "__all__"


class BearbeiterListFilter(django_filters.FilterSet):

    class Meta:
        model = Bearbeiter
        fields = "__all__"
