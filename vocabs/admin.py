from django.contrib import admin
from .models import *

admin.site.register(SkosLabel)
admin.site.register(SkosConcept)
admin.site.register(SkosRelation)
admin.site.register(SkosNamespace)
