from django.core.exceptions import ValidationError
from django.test import TestCase
from initiative.models import Initiative, Encounter
from unittest import skip


class EncounterAndInitiativeModelTest(TestCase):

    def test_save_initiative_object_and_retrieve(self):
        encounter_ = Encounter()
        encounter_.save()

        first_init = Initiative()
        first_init.creature_name = 'Shaltorin'
        first_init.initiative_value = 20
        first_init.hit_points = 250
        first_init.encounter = encounter_
        first_init.save()

        second_init = Initiative()
        second_init.creature_name = 'Falkrainne'
        second_init.initiative_value = 1
        second_init.hit_points = 2
        second_init.encounter = encounter_
        second_init.save()

        init_order = Initiative.objects.all()
        self.assertEqual(init_order.count(), 2)

        saved_encounter = Encounter.objects.first()
        self.assertEqual(saved_encounter, encounter_)

        first_saved_init = init_order[0]
        second_saved_init = init_order[1]

        self.assertEqual(first_saved_init.creature_name, first_init.creature_name)
        self.assertEqual(first_saved_init.initiative_value, first_init.initiative_value)
        self.assertEqual(first_saved_init.hit_points, first_init.hit_points)

        self.assertEqual(second_saved_init.creature_name, second_init.creature_name)
        self.assertEqual(second_saved_init.initiative_value, second_init.initiative_value)
        self.assertEqual(second_saved_init.hit_points, second_init.hit_points)

    @skip
    def test_cannot_save_initiative_without_init_value(self):
        # need to sort out a way to test this, not sure given the data type
        pass

    def test_cannot_save_initiative_without_name_value(self):
        encounter_ = Encounter.objects.create()

        initiative_ = Initiative(creature_name='', initiative_value=9,
                                 hit_points=100, encounter=encounter_)
        with self.assertRaises(ValidationError):
            initiative_.save()
            initiative_.full_clean()