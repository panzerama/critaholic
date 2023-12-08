from django import forms
from .models import Initiative


class InitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        fields = ['creature_name', 'initiative_value', 'hit_points']
