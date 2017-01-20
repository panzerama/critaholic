from django.test import TestCase
from character.views import char_page
from django.core.urlresolvers import resolve

class CharacterViewTest(TestCase):

    def test_character_view_uses_template(self):
        found = resolve('/character/')
        self.assertEqual(found.func, char_page)

    def test_character_home_page_uses_correct_template(self):
        response = self.client.get('/character/')
        self.assertTemplateUsed(response, 'char_home.html')