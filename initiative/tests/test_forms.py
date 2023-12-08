from django.test import TestCase
from initiative.forms import InitiativeForm


class InitiativeTestForm(TestCase):

    def test_initiative_form_renders_correct_css(self):
        init_form = InitiativeForm()
        self.assertIn('id="id_creature_name"', init_form.as_p())
        self.assertIn('id="id_initiative_value"', init_form.as_p())
        self.assertIn('id="id_hit_points"', init_form.as_p())

    def test_initiative_form_validates_input(self):
        data = {'creature_name': '', 'initiative_value': 9, 'hit_points': 100}
        init_form = InitiativeForm(data=data)
        self.assertFalse(init_form.is_valid())
        self.assertEqual
