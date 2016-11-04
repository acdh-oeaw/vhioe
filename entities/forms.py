from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Band


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BandForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Speichern'))
