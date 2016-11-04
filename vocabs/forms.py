from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import (
    EinbringerGechlecht, Eingangsart, Geschaeftsbereich, Erledigungsart, Beruf)


class EinbringerGechlechtForm(forms.ModelForm):
    class Meta:
        model = EinbringerGechlecht
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EinbringerGechlechtForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))


class EingangsartForm(forms.ModelForm):
    class Meta:
        model = Eingangsart
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EingangsartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))


class GeschaeftsbereichForm(forms.ModelForm):
    class Meta:
        model = Geschaeftsbereich
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GeschaeftsbereichForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))


class ErledigungsartForm(forms.ModelForm):
    class Meta:
        model = Erledigungsart
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ErledigungsartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))


class BerufForm(forms.ModelForm):
    class Meta:
        model = Beruf
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BerufForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))
