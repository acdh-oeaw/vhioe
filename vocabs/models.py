from django.db import models
from labels.models import Label


class VocabsBaseClass(models.Model):
    name = models.CharField(max_length=300, blank=True)
    alternative_namen = models.ManyToManyField(Label, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.name)


class EinbringerGechlecht(VocabsBaseClass):

    """Holds information about a person's gender"""

    pass


class Eingangsart(VocabsBaseClass):

    """A classification for the entries."""

    pass


class Geschaeftsbereich(VocabsBaseClass):

    """Field of administration the entry is related to."""

    pass


class Erledigungsart(VocabsBaseClass):

    """Describes what has to happen to solve the issues adressed in the entry"""

    pass


class Beruf(VocabsBaseClass):

    """Describes what has to happen to solve the issues adressed in the entry"""

    pass
