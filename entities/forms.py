from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Band, Archiv, Institution, Person, Bearbeiter


class BearbeiterForm(forms.ModelForm):
    class Meta:
        model = Bearbeiter
        fields = [
            'name', 'vorname', 'bearbeiter_kuerzel', 'institution',
            'sex', 'beruf', 'ort', 'gnd_id', 'akronym'
        ]
        widgets = {
            'ort': autocomplete.ModelSelect2(
                url='entities:ort-autocomplete'),
            'beruf': autocomplete.ModelSelect2(
                url='vocabs-ac:skosconcept-autocomplete'),
            'institution': autocomplete.ModelSelect2Multiple(
                url='entities:institution-autocomplete'
            )
        }

    def __init__(self, *args, **kwargs):
        super(BearbeiterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'Speichern'))


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'vorname', 'sex', 'beruf', 'ort', 'gnd_id', 'akronym']
        widgets = {
            'ort': autocomplete.ModelSelect2(
                url='entities:ort-autocomplete'),
            'beruf': autocomplete.ModelSelect2(
                url='vocabs-ac:skosconcept-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'Speichern'))


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
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
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
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
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
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'Speichern'))
