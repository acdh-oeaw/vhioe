from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Eintrag


class EintragForm(forms.ModelForm):
    class Meta:
        model = Eintrag
        fields = "__all__"
        widgets = {
            'band': autocomplete.ModelSelect2(
                url='entities:band-autocomplete'),
            'bearbeiter': autocomplete.ModelSelect2(
                url='entities:bearbeiter-autocomplete'),
            'klient_institution': autocomplete.ModelSelect2Multiple(
                url='entities:institution-autocomplete'),
            'einbringer_berufsgruppe': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'einbringer_geschlecht': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'klient_person': autocomplete.ModelSelect2Multiple(
                url='entities:person-autocomplete'),
            'eingangsart': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'geschaeftsbereich': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'vorakten_erfasst': autocomplete.ModelSelect2Multiple(
                url='entries:eintrag-autocomplete'),
            'erledigungs_art': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'erledigende_institution': autocomplete.ModelSelect2Multiple(
                url='entities:institution-autocomplete'),
            'erledigende_person': autocomplete.ModelSelect2Multiple(
                url='entities:person-autocomplete'),
            'nachakten_erfasst': autocomplete.ModelSelect2Multiple(
                url='entries:eintrag-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(EintragForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
