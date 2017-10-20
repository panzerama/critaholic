from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from initiative.models import Initiative, Encounter
from unittest import skip


class EncounterAndInitiativeModelTest(TestCase):

    def test_save_initiative_object_and_retrieve(self):
        encounter_ = Encounter()
        encounter_.save()

        first_init = Initiative()
        first_init.creature_name = 'Shaltorinn'
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

    def test_cannot_save_initiative_without_init_value(self):
        encounter_ = Encounter.objects.create()

        initiative_ = Initiative(creature_name='Shaltorinn', initiative_value=None,
                                 hit_points=100, encounter=encounter_)
        with self.assertRaises(IntegrityError):
            initiative_.save()
            initiative_.full_clean()

    def test_cannot_save_initiative_without_name_value(self):
        encounter_ = Encounter.objects.create()

        initiative_ = Initiative(creature_name='', initiative_value=9,
                                 hit_points=100, encounter=encounter_)
        with self.assertRaises(ValidationError):
            initiative_.save()
            initiative_.full_clean()

    def test_get_absolute_url(self):
        encounter_ = Encounter.objects.create()

        self.assertEqual(encounter_.get_absolute_url(), '/init/%d/' % encounter_.id)

    def test_initiative_order_assigned_automatically(self):
        encounter_ = Encounter()
        encounter_.save()

        first_init = Initiative()
        first_init.creature_name = 'Falkrainne'
        first_init.initiative_value = 1
        first_init.hit_points = 250
        first_init.encounter = encounter_
        first_init.save()

        second_init = Initiative()
        second_init.creature_name = 'Shaltorinn'
        second_init.initiative_value = 20
        second_init.hit_points = 210
        second_init.encounter = encounter_
        second_init.save()

        init_order = Initiative.objects.all()
        first_saved_init = init_order[0]
        second_saved_init = init_order[1]

        self.assertEqual(first_saved_init.turn_order, 1)
        self.assertEqual(first_saved_init.creature_name, 'Falkrainne')
        self.assertEqual(second_saved_init.turn_order, 2)
        self.assertEqual(second_saved_init.creature_name, 'Shaltorinn')

    def test_initiative_sort_function_modifies_turn_order(self): #todo remove code duplication
        encounter_ = Encounter()
        encounter_.save()

        first_init = Initiative()
        first_init.creature_name = 'Falkrainne'
        first_init.initiative_value = 1
        first_init.hit_points = 250
        first_init.encounter = encounter_
        first_init.save()

        second_init = Initiative()
        second_init.creature_name = 'Shaltorinn'
        second_init.initiative_value = 20
        second_init.hit_points = 210
        second_init.encounter = encounter_
        second_init.save()

        third_init = Initiative()
        third_init.creature_name = 'Kobold'
        third_init.initiative_value = 15
        third_init.hit_points = 12
        third_init.encounter = encounter_
        third_init.save()

        init_order = Initiative.objects.all()
        first_saved_init = init_order[0]
        second_saved_init = init_order[1]
        third_saved_init = init_order[2]

        self.assertEqual(first_saved_init.turn_order, 1)
        self.assertEqual(first_saved_init.creature_name, 'Falkrainne')
        self.assertEqual(second_saved_init.turn_order, 2)
        self.assertEqual(second_saved_init.creature_name, 'Shaltorinn')
        self.assertEqual(third_saved_init.turn_order, 3)
        self.assertEqual(third_saved_init.creature_name, 'Kobold')