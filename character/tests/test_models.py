from django.test import TestCase
from character.models import Character


class CharacterModelTest(TestCase):

    def test_character_save_and_retrieve(self):
        new_character = Character()
        new_character.character_name = 'Shaltorinn'
        new_character.summary = 'Gold-plated boy scout.'
        new_character.save()

        party = Character.objects.all()
        self.assertEqual(party.count(), 1)

        party_leader = Character.objects.first()
        self.assertEqual(party_leader.character_name, new_character.character_name)
        self.assertEqual(party_leader.summary, new_character.summary)
