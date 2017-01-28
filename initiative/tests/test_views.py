from django.core.urlresolvers import resolve
from django.test import TestCase
from initiative.models import Initiative, Encounter
import math


class NewEncounterTest(TestCase):

    def test_name_and_init_input_saved_by_POST(self):
        self.client.post('/init/new', data={'init_name': 'beholder', 'init_num': 18, 'init_hp': 150})

        self.assertEqual(Initiative.objects.count(), 1)
        new_init_order = Initiative.objects.first()
        self.assertEqual(new_init_order.creature_name, 'beholder')
        self.assertEqual(new_init_order.initiative_value, 18)

    def test_new_encounter_redirects_after_POST(self):
        response = self.client.post('/init/new', data={'init_name': 'beholder', 'init_num': 18, 'init_hp': 150})

        self.assertEqual(response.status_code, 302)

        new_encounter = Encounter.objects.first()
        self.assertEqual(response['location'], '/init/%d/' % (new_encounter.id,))

    def test_empty_initiative_name_passes_error_to_new_encounter(self):
        response = self.client.post('/init/new', data={'init_name': '', 'init_num': 18, 'init_hp': 150})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = 'An initiative entry must have a name!'
        self.assertContains(response, expected_error)

    def test_invalid_initiative_items_not_saved(self):
        self.client.post('/init/new', data={'init_name': '', 'init_num': 18, 'init_hp': 150})

        self.assertEqual(Encounter.objects.count(), 0)
        self.assertEqual(Initiative.objects.count(), 0)


class InitViewTest(TestCase):

    def test_uses_view_init_template(self):
        encounter_ = Encounter.objects.create()
        response = self.client.get('/init/%d/' % (encounter_.id,))
        self.assertTemplateUsed(response, 'view_init.html')

    def test_displays_all_monsters_in_order(self):
        correct_encounter_ = Encounter.objects.create()
        Initiative.objects.create(creature_name='beholder', initiative_value=10, hit_points=150, encounter=correct_encounter_)
        Initiative.objects.create(creature_name='displacer beast', initiative_value=11, hit_points=100, encounter=correct_encounter_)


        incorrect_encounter_ = Encounter.objects.create()
        Initiative.objects.create(creature_name='Shaltorin', initiative_value=20, hit_points=250, encounter=incorrect_encounter_)
        Initiative.objects.create(creature_name='Falkrainne', initiative_value=1, hit_points=2, encounter=incorrect_encounter_)

        response = self.client.get('/init/%d/' % (correct_encounter_.id,))

        self.assertContains(response, 'beholder')
        self.assertContains(response, '10')
        self.assertContains(response, '150')
        self.assertContains(response, 'displacer beast')
        self.assertContains(response, '11')
        self.assertContains(response, '100')

        self.assertNotContains(response, 'Shaltorin')
        self.assertNotContains(response, 'Falkrainne')

    def test_init_view_uses_correct_encounter_id(self):
        correct_encounter_ = Encounter.objects.create()
        incorrect_encounter_ = Encounter.objects.create()
        response = self.client.get('/init/%d/' % (correct_encounter_.id,))
        self.assertEqual(response.context['encounter'], correct_encounter_)

    def test_can_save_initiative_to_existing_encounter(self):
        other_encounter = Encounter.objects.create()
        this_encounter = Encounter.objects.create()

        self.client.post('/init/%d/' % (this_encounter.id,),
                         data={'init_name': 'beholder', 'init_num': 18, 'init_hp': 150})

        self.assertEqual(Initiative.objects.count(), 1)
        new_init = Initiative.objects.first()
        self.assertEqual(new_init.creature_name, 'beholder')
        self.assertEqual(new_init.encounter, this_encounter)

    def test_POST_redirects_to_initiative_view(self):
        other_encounter = Encounter.objects.create()
        this_encounter = Encounter.objects.create()

        response = self.client.post('/init/%d/' % (this_encounter.id,),
                                    data={'init_name': 'beholder', 'init_num': 18, 'init_hp': 150})

        self.assertRedirects(response, '/init/%d/' % (this_encounter.id,))

    def test_init_name_validation_errors_displayed_on_init_view(self):
        encounter_ = Encounter.objects.create()
        response = self.client.post('/init/%d/' % encounter_.id, data={'init_name': '', 'init_num': 18, 'init_hp': 150})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_init.html')
        expected_error = 'An initiative entry must have a name!'
        self.assertContains(response, expected_error)


class HPModifyTest(TestCase):

    def test_hp_add_redirects_and_modifies_init(self):
        this_encounter = Encounter.objects.create()
        this_initiative = Initiative.objects.create(creature_name='Shaltorin', initiative_value=20, hit_points=250,
                                                    encounter=this_encounter)

        response = self.client.post('/init/%d/%d/hp_add' % (this_encounter.id, this_initiative.id,),
                                    data={'Shaltorin_hp_value': '5'})

        self.assertRedirects(response, '/init/%d/' % (this_encounter.id,))

        shaltorin_hp = Initiative.objects.get(id=this_initiative.id).hit_points

        self.assertEqual(255, shaltorin_hp)

    def test_hp_sub_redirects_and_modifies_init(self):
        other_encounter = Encounter.objects.create()
        this_encounter = Encounter.objects.create()
        this_initiative = Initiative.objects.create(creature_name='Shaltorin', initiative_value=20, hit_points=250,
                                                    encounter=this_encounter)

        response = self.client.post('/init/%d/%d/hp_sub' % (this_encounter.id, this_initiative.id,),
                                    data={'Shaltorin_hp_value': '5'})

        self.assertRedirects(response, '/init/%d/' % (this_encounter.id,))

        shaltorin_hp = Initiative.objects.get(id=this_initiative.id).hit_points

        self.assertEqual(245, shaltorin_hp)
