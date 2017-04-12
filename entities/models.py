from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept
from places.models import Place


class EntityBaseClass(models.Model):
    name = models.CharField(
        max_length=300, blank=True,
        help_text="Name of the entity")
    akronym = models.CharField(max_length=25, blank=True, help_text="some akronym")
    ort = models.ForeignKey(
        Place, max_length=200, blank=True, null=True, help_text="Place entity is related to.")
    gnd_id = models.CharField(max_length=50, blank=True, help_text="gnd-identifier")

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.name)


class Archiv(EntityBaseClass):

    """Holds information about the archive"""

    def __str__(self):
        if self.akronym is not "":
            return "{}".format(self.akronym)
        else:
            return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('entities:archiv_detail', kwargs={'pk': self.id})


class Institution(EntityBaseClass):

    """Holds information about an institution which has to deal with an entry."""

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('entities:institution_detail', kwargs={'pk': self.id})


class Person(EntityBaseClass):

    """Persons mentioned in the entries. One entry can contain many persons"""

    GENDER_CHOICES = (
        ('männlich', 'männlich'),
        ('weiblich', 'weiblich'),
        ('unbekannt', 'unbekannt'),
    )
    sex = models.CharField(
        blank=True, max_length=150, help_text="Sex", choices=GENDER_CHOICES)
    vorname = models.CharField(
        blank=True, max_length=150, help_text="Vorname des Klienten")
    beruf = models.ForeignKey(SkosConcept, blank=True, null=True)

    def __str__(self):
        return "{} | {} | {}, {} | {}".format(
            self.sex, self.ort, self.name, self.vorname, self.beruf)

    def get_absolute_url(self):
        return reverse('entities:person_detail', kwargs={'pk': self.id})


class Bearbeiter(Person):

    """  Administrative personnel which created an entry (Eintrag) """

    bearbeiter_kuerzel = models.CharField(
        blank=True, max_length=150, help_text="Kürzel des Sachbearbeiters")
    institution = models.ManyToManyField(
        Institution, blank=True, help_text="Institution des Bearbeiters")

    def __str__(self):
        return "({}) {}".format(
            self.bearbeiter_kuerzel, "_".join([str(x) for x in self.institution.all()]))


class Band(models.Model):

    """Contains information about the archival unit.
    One Band contains many entries"""

    archiv = models.ForeignKey(
        Archiv, blank=True, null=True, max_length=150, help_text="Name des Archives")
    bestand = models.CharField(
        blank=True, max_length=150, help_text="Bestandsbezeichnung")
    jahr = models.PositiveIntegerField(blank=True, null=True, help_text="Jahr")
    signatur = models.CharField(verbose_name="Distinktionszeichen", max_length=250, blank=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.archiv, self.bestand, self.jahr, self.signatur)

    def get_absolute_url(self):
        return reverse('entities:band_detail', kwargs={'pk': self.id})
