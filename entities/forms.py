from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Band, Archiv, Institution


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = "__all__"
        widgets = {
            'archiv': autocomplete.ModelSelect2(
                url='entities:archiv-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(BandForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))


class ArchivForm(forms.ModelForm):
    class Meta:
        model = Archiv
        fields = "__all__"
        widgets = {
            'ort': autocomplete.ModelSelect2(
                url='entities:ort-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(ArchivForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"
        widgets = {
            'ort': autocomplete.ModelSelect2(
                url='entities:ort-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))
