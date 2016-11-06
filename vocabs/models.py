import os
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


DEFAULT_PEFIX = os.path.basename(settings.BASE_DIR)

DEFAULT_NAMESPACE = "http://www.vocabs/{}/".format(DEFAULT_PEFIX)

LABEL_TYPES = (
    ('prefLabel', 'prefLabel'),
    ('altLabel', 'altLabel'),
    ('hiddenLabel', 'hiddenLabel'),
)

RELATION_TYPES = (
    ('narrower', 'narrower'),
    ('broader', 'broader'),
    ('related', 'related'),
    ('broadMatch', 'broadMatch'),
    ('relatedMatch', 'relatedMatch'),
    ('exactMatch', 'exactMatch'),
)


class SkosNamespace(models.Model):
    namespace = models.URLField(blank=True, default=DEFAULT_NAMESPACE)
    prefix = models.CharField(max_length=50, blank=True, default=DEFAULT_PEFIX)

    def __str__(self):
        return "{}".format(self.prefix)


class SkosConceptScheme(models.Model):
    dc_title = models.CharField(max_length=300, blank=True)
    namespace = models.ForeignKey(SkosNamespace, blank=True, null=True)
    dct_creator = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if self.namespace is None:
            temp_namespace, _ = SkosNamespace.objects.get_or_create(
                namespace=DEFAULT_NAMESPACE, prefix=DEFAULT_PEFIX)
            temp_namespace.save()
            self.namespace = temp_namespace
        else:
            pass
        super(SkosConceptScheme, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vocabs:skosconceptscheme_detail', kwargs={'pk': self.id})


class SkosLabel(models.Model):
    label = models.CharField(max_length=100, blank=True, help_text="The entities label or name.")
    label_type = models.CharField(
        max_length=30, blank=True, choices=LABEL_TYPES, help_text="The type of the label.")
    isoCode = models.CharField(
        max_length=3, blank=True, help_text="The ISO 639-3 code for the label's language.")

    def __str__(self):
        if self.label_type != "":
            return "{} @{} ({})".format(self.label, self.isoCode, self.label_type)
        else:
            return "{} @{})".format(self.label, self.isoCode)


class SkosConcept(models.Model):
    pref_label = models.CharField(max_length=300, blank=True)
    pref_label_lang = models.CharField(max_length=3, blank=True, default="eng")
    definition = models.TextField(blank=True)
    definition_lang = models.CharField(max_length=3, blank=True, default="eng")
    label = models.ManyToManyField(SkosLabel, blank=True)
    notation = models.CharField(max_length=300, blank=True, unique=True)
    namespace = models.ForeignKey(SkosNamespace, blank=True, null=True)
    scheme = models.ManyToManyField(SkosConceptScheme, blank=True)

    def save(self, *args, **kwargs):
        temp_notation = slugify(self.pref_label, allow_unicode=True)
        concepts = len(SkosConcept.objects.filter(notation=temp_notation))
        if concepts < 1:
            self.notation = temp_notation
        else:
            self.notation = "{}-{}".format(temp_notation, concepts)

        if self.namespace is None:
            temp_namespace, _ = SkosNamespace.objects.get_or_create(
                namespace=DEFAULT_NAMESPACE, prefix=DEFAULT_PEFIX)
            temp_namespace.save()
            self.namespace = temp_namespace
        else:
            pass

        super(SkosConcept, self).save(*args, **kwargs)

    def __str__(self):
        return "{} ({}:{})".format(self.pref_label, self.namespace, self.notation)

    def get_absolute_url(self):
        return reverse('vocabs:skosconcept_detail', kwargs={'pk': self.id})


class SkosRelation(models.Model):
    concept_a = models.ForeignKey(SkosConcept, related_name="first_concept")
    concept_b = models.ForeignKey(SkosConcept, related_name="second_concept")
    relation_type = models.CharField(choices=RELATION_TYPES, max_length=30)
    owl_inverseOf = models.CharField(blank=True, null=True, max_length=30)

    def save(self, *args, **kwargs):
        if self.relation_type == "narrower":
            self.owl_inverseOf = "broader"
        elif self.relation_type == "broader":
            self.owl_inverseOf = "narrower"
        elif self.relation_type == "related":
            self.owl_inverseOf = "related"
        elif self.relation_type == "broadMatch":
            self.owl_inverseOf = "broadMatch"
        elif self.relation_type == "relatedMatch":
            self.owl_inverseOf = "relatedMatch"
        elif self.relation_type == "exactMatch":
            self.owl_inverseOf = "exactMatch"
        super(SkosRelation, self).save(*args, **kwargs)

    def __str__(self):
        return "{} is {} as {}".format(
            self.concept_a, self.relation_type, self.concept_b)
