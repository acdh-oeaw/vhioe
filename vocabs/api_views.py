from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import SkosConcept, SkosConceptScheme, SkosLabel, SkosNamespace
from .serializers import (
    SkosLabelSerializer, SkosNamespaceSerializer, SkosConceptSchemeSerializer, SkosConceptSerializer
)
from .filters import SkosConceptFilter


class SkosLabelViewSet(viewsets.ModelViewSet):

    queryset = SkosLabel.objects.all()
    serializer_class = SkosLabelSerializer


class SkosNamespaceViewSet(viewsets.ModelViewSet):

    queryset = SkosNamespace.objects.all()
    serializer_class = SkosNamespaceSerializer


class SkosConceptSchemeViewSet(viewsets.ModelViewSet):

    queryset = SkosConceptScheme.objects.all()
    serializer_class = SkosConceptSchemeSerializer


class SkosConceptViewSet(viewsets.ModelViewSet):

    queryset = SkosConcept.objects.all()
    serializer_class = SkosConceptSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SkosConceptFilter