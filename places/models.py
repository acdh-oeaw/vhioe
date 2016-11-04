from django.db import models
from labels.models import Label


class Place(models.Model):

    """Holds information about places."""
    name = models.CharField(
        max_length=250, blank=True, help_text="Normalisierte, gegenwärtige Ortsbezeichnung")
    alternative_name = models.ManyToManyField(
        Label, max_length=250, blank=True,
        help_text="Alternative names")
    geonames_id = models.CharField(max_length=50, blank=True, help_text="GND-ID")
    lat = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    lng = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
