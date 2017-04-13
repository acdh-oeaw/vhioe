from django.db import models
from vocabs.models import SkosLabel, SkosConcept


class Place(models.Model):

    """Holds information about places."""
    name = models.CharField(
        max_length=250, blank=True, help_text="Normalisierte, gegenwärtige Ortsbezeichnung")
    alternative_name = models.ManyToManyField(
        SkosLabel, max_length=250, blank=True,
        help_text="Alternative names")
    geonames_id = models.CharField(max_length=50, blank=True)
    lat = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    lng = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    part_of = models.ForeignKey(
        "Place", null=True, blank=True, help_text="A place (country) this place is part of."
    )
    place_type = models.ForeignKey(SkosConcept, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
