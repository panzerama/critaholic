from django import forms
from django.forms import ModelForm
from .models import Initiative


class InitiativeForm(ModelForm):

    class Meta:
        model = Initiative
        fields = ['creature_name', 'initiative_value', 'hit_points']

        attrs = {'class': 'col-md-4 form-group'}
        widgets = {'creature_name': forms.TextInput(attrs=attrs),
                   'initiative_value': forms.TextInput(attrs=attrs),
                   'hit_points': forms.TextInput(attrs=attrs)}