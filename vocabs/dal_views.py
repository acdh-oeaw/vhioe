from dal import autocomplete
from .models import SkosLabel, SkosConceptScheme


class SkosLabelAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosLabel.objects.all()

        if self.q:
            qs = qs.filter(label__icontains=self.q)

        return qs


class SkosConceptSchemeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosConceptScheme.objects.all()

        if self.q:
            qs = qs.filter(dc_title__icontains=self.q)

        return qs
