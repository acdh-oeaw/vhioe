# -*- coding: utf-8 -*-
from django import forms
from dal import autocomplete
from crispy_forms.helper import FormHelper
from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        widgets = {
            'alternative_name': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skoslabel-autocomplete'
            ),
            'part_of': autocomplete.ModelSelect2(
                url='entities:ort-autocomplete'),
            'place_type': autocomplete.ModelSelect2(
                url='vocabs-ac:skosconcept-autocomplete'),
            }

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
