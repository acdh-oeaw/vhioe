from django.db import models
from entities.models import *
from vocabs.models import *


class Eintrag(models.Model):

    """ Contains information about the administrative work."""

    band = models.ForeignKey(Band, blank=True, null=True, help_text="Band")
    aktenzahl = models.CharField(
        primary_key=True, unique=True, max_length=150,
        help_text="Kombination aus Archivkürzel_Jahr_Aktenzahl")
    faksimile = models.CharField(
        blank=True, null=True, max_length=150,
        help_text="Name der Datei, auf der das Faksimile gespeichert ist.")
    eingangsdatum = models.DateField(
        blank=True, null=True,
        help_text="Eingangsdatum: Datumsangaben bitte im Format YYYY-MM-DD angeben")
    bearbeiter = models.ForeignKey(Bearbeiter, blank=True, null=True, help_text="Sachbearbeiter")
    klient_institution = models.ManyToManyField(
        Institution, blank=True, help_text="Institution, von der Eingangsstück ausgeht",
        related_name="institution_klient",
        verbose_name="Einbringer (Institution)")
    einbringer = models.NullBooleanField(
        null=True, default=False,
        help_text="Handelt es sich beim 'Einbringer' um eine Person (Ja/Nein).")
    einbringer_berufsgruppe = models.ForeignKey(
        Beruf, blank=True, null=True,
        help_text="Berufsgruppe, welcher die einbringede Person zugeordnet werde kann")
    einbringer_geschlecht = models.ForeignKey(
        EinbringerGechlecht, blank=True, null=True, help_text="PLEASEPROVIDESOMEHELPTEXT")
    klient_person = models.ManyToManyField(
        Person, blank=True,
        help_text="Person, von der Eingangsstück ausgeht",
        related_name="person_klient",
        verbose_name="Einbringer (Person)")
    eingangsart = models.ForeignKey(
        Eingangsart, blank=True, null=True, help_text="Art des Eingangs")
    geschaeftsbereich = models.ForeignKey(
        Geschaeftsbereich, blank=True, null=True, help_text="Art des Eingangs")
    aktenzahl_anfragende_behoerde = models.CharField(
        blank=True, null=True, max_length=150,
        help_text="Aktenzahl des Eingangsstücks bei der einbringenden Behörde",
        verbose_name="Aktenzahl Einbringer")
    datum_akt_anfragende_behoerde = models.DateField(
        blank=True, null=True, verbose_name="Datum Einbringer",
        help_text="Ausstellungsdatum des Eingangsstücks. Bitte im Format YYYY-MM-DD angeben")
    vorakten_erfasst = models.ManyToManyField(
        "Eintrag", blank=True, help_text="Aktenzahlen von Vorakten", related_name='eintrag_vorakt')
    vorakten_nichterfast = models.CharField(
        blank=True, max_length=300,
        help_text="Signatur von Vorakten, die nicht von der Datenbank erfasst werden.")
    frist = models.DateField(
        blank=True, null=True,
        help_text="Zur Beantwortung vorgegebene Frist. Bitte im Format YYYY-MM-DD angeben")
    erledigungs_art = models.ForeignKey(
        Erledigungsart, blank=True, null=True,
        help_text="Art der Erledigung durch Bezirksbehörde.")
    erledigende_institution = models.ManyToManyField(
        Institution, blank=True, help_text="Institution, an die sich Erledigung richtet",
        related_name="institution_erledigt",
        verbose_name="„Empfänger (Institution)")
    erledigende_person = models.ManyToManyField(
        Person, blank=True,
        help_text="Person, an die sich Erledigung richtet.",
        related_name="person_erledigt",
        verbose_name="Empfänger (Person)")
    erledigungsdatum = models.DateField(
        blank=True, null=True,
        help_text="Datum der Erledigung: Datumsangaben bitte im Format YYYY-MM-DD angeben")
    nachakten_erfasst = models.ManyToManyField(
        "Eintrag", blank=True, help_text="Aktenzahlen von Nachakten.",
        related_name='eintrag_nachakt')
    nachackten_nichterfast = models.CharField(
        blank=True, max_length=300,
        help_text="Signatur von Nachackten, die nicht von der Datenbank erfasst werden.")
    ablage = models.CharField(
        blank=True, null=True, max_length=100,
        help_text="Ablageplaninformation")
