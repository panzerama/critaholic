from django.test import TestCase
from character.views import home_page
from django.core.urlresolvers import resolve

class CharacterViewTest(TestCase):

    def test_character_view_uses_template(self):
        found = resolve('/character')
        self.assertEqual(found.func, home_page)