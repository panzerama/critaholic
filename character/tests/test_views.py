from django.test import TestCase
from character.views import char_page
from django.urls import resolve
from character.models import Character

class NewCharacterTest(TestCase):

    def test_character_view_uses_template(self):
        found = resolve('/character/')
        self.assertEqual(found.func, char_page)

    def test_character_home_page_uses_correct_template(self):
        response = self.client.get('/character/')
        self.assertTemplateUsed(response, 'char_home.html')

    def test_new_character_redirects_after_POST(self):
        response = self.client.post('/character/new', data={'character_name': 'Shaltorinn',
                                                            'character_description': 'Golden Boy Scout'})

        self.assertEqual(response.status_code, 302)

        new_character = Character.objects.first()
        self.assertEqual(response['location'], '/character/%d/' % (new_character.id,))