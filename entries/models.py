from django.db import models
from vocabs.models import SkosConcept
from django.core.urlresolvers import reverse
from entities.models import *
from places.models import Place


class Eintrag(models.Model):

    """ Contains information about the administrative work."""

    band = models.ForeignKey(Band, blank=True, null=True, help_text="Band")
    aktenzahl = models.CharField(
        max_length=150, help_text="Kombination aus Archivkürzel_Jahr_Aktenzahl")
    faksimile = models.CharField(
        blank=True, max_length=150,
        help_text="Name der Datei, auf der das Faksimile gespeichert ist.")
    eingangsdatum = models.DateField(
        blank=True, null=True,
        help_text="Eingangsdatum: Datumsangaben bitte im Format YYYY-MM-DD angeben")
    bearbeiter = models.ForeignKey(Bearbeiter, blank=True, null=True, help_text="Sachbearbeiter")
    klient_institution = models.ManyToManyField(
        Institution, blank=True, help_text="Institution, von der Eingangsstück ausgeht",
        related_name="institution_klient",
        verbose_name="Einbringende Institution")
    einbringer = models.NullBooleanField(
        null=True, default=False, verbose_name="Einbringer*in",
        help_text="Geht das Eingangsstück von einer Person aus (Ja/Nein)")
    einbringer_ort = models.ForeignKey(
        Place, blank=True, null=True, verbose_name="Einbringer*in Ort",
        help_text="Wohn- oder Aufenthaltsort der einbringenden Person"
    )
    einbringer_berufsgruppe = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="einbringer_beruf_skos",
        help_text="Berufsgruppe, der die einbringende Person zugeordnet werden kann",
        verbose_name="Einbringer*in Berufsgruppe")
    einbringer_geschlecht = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="einbringer_geschlecht_skos",
        verbose_name="Einbringer*in Geschlecht",
        help_text="Angegebenes Geschlecht der einbringenden Person")
    klient_person = models.ManyToManyField(
        Person, blank=True,
        help_text="Person, von der Eingangsstück ausgeht",
        related_name="person_klient",
        verbose_name="Einbringer*in Person")
    eingangsart = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="Art des Eingangs",
        related_name="eingangsart_skos")
    geschaeftsbereich = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="Sachbereich des Betreffs",
        related_name="geschaeftsbereich_skos", verbose_name="Geschäftsbereich")
    aktenzahl_anfragende_behoerde = models.CharField(
        blank=True, max_length=150,
        help_text="Aktenzahl des Eingangsstücks bei der einbringenden Behörde",
        verbose_name="Aktenzahl Einbringer")
    datum_akt_anfragende_behoerde = models.DateField(
        blank=True, null=True, verbose_name="Datum Einbringer",
        help_text="Ausstellungsdatum des Eingangsstücks. Bitte im Format YYYY-MM-DD angeben")
    vorakten_erfasst = models.ManyToManyField(
        "Eintrag", blank=True, help_text="Aktenzahlen von Vorakten", related_name='eintrag_vorakt',
        verbose_name="Vorakten erfasst")
    vorakten_nichterfast = models.CharField(
        blank=True, max_length=300, verbose_name="Vorakten nicht erfasst",
        help_text="Signatur von Vorakten, die nicht von der Datenbank erfasst werden.")
    frist = models.DateField(
        blank=True, null=True,
        help_text="Zur Beantwortung vorgegebene Frist. Bitte im Format YYYY-MM-DD angeben")
    erledigungs_art = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="erledigungs_art_skos",
        help_text="Art der Erledigung durch Bezirksbehörde.", verbose_name="Erledigungsart")
    erledigende_institution = models.ManyToManyField(
        Institution, blank=True, help_text="Institution, an die sich Erledigung richtet",
        related_name="institution_erledigt",
        verbose_name="Empfangende Institution")
    erledigende_person = models.ManyToManyField(
        Person, blank=True,
        help_text="Person, an die sich Erledigung richtet.",
        related_name="person_erledigt",
        verbose_name="Empfänger*in Person")
    erledigungsdatum = models.DateField(
        blank=True, null=True,
        help_text="Datum der Erledigung: Datumsangaben bitte im Format YYYY-MM-DD angeben")
    nachakten_erfasst = models.ManyToManyField(
        "Eintrag", blank=True, help_text="Aktenzahlen von Nachakten.",
        related_name='eintrag_nachakt', verbose_name="Nachakten erfasst")
    nachackten_nichterfast = models.CharField(
        blank=True, max_length=300, verbose_name="Nachakten nicht erfasst",
        help_text="Signatur von Nachakten, die nicht von der Datenbank erfasst werden.")
    ablage = models.CharField(
        blank=True, max_length=100,
        help_text="Ablageplaninformation")

    def __str__(self):
        return "{}, {}".format(self.band, self.aktenzahl)

    def get_absolute_url(self):
        return reverse('entries:eintrag_detail', kwargs={'pk': self.id})
