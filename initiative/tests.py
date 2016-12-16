from django.core.urlresolvers import resolve
from django.test import TestCase
from initiative.views import home_page
from initiative.models import Initiative, Encounter


class HomePageTest(TestCase):

    # TODO later on, change the home page to a menu system and move this to '/init'
    def test_root_url_uses_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class NewEncounterTest(TestCase):

    def test_name_and_init_input_saved_by_POST(self):
        self.client.post('/init/new', data={'init_name': 'beholder', 'init_num': 18})

        self.assertEqual(Initiative.objects.count(), 1)
        new_init_order = Initiative.objects.first()
        self.assertEqual(new_init_order.creature_name, 'beholder')
        self.assertEqual(new_init_order.initiative_value, 18)

    def test_new_encounter_redirects_after_POST(self):
        response = self.client.post('/init/new', data={'init_name': 'beholder', 'init_num': 18})

        self.assertEqual(response.status_code, 302)

        new_encounter = Encounter.objects.first()
        self.assertEqual(response['location'], '/init/%d/' % (new_encounter.id,))


class InitViewTest(TestCase):

    def test_uses_init_view_template(self):
        encounter_ = Encounter.objects.create()
        response = self.client.get('/init/%d/' % (encounter_.id,))
        self.assertTemplateUsed(response, 'init_view.html')

    def test_displays_all_monsters_in_order(self):
        correct_encounter_ = Encounter.objects.create()
        Initiative.objects.create(creature_name='beholder', initiative_value=10, encounter=correct_encounter_)
        Initiative.objects.create(creature_name='displacer beast', initiative_value=11, encounter=correct_encounter_)

        incorrect_encounter_ = Encounter.objects.create()
        Initiative.objects.create(creature_name='Shaltorin', initiative_value=20, encounter=incorrect_encounter_)
        Initiative.objects.create(creature_name='Falkrainne', initiative_value=1, encounter=incorrect_encounter_)

        response = self.client.get('/init/%d/' % (correct_encounter_.id,))

        self.assertContains(response, 'beholder')
        self.assertContains(response, '10')
        self.assertContains(response, 'displacer beast')
        self.assertContains(response, '11')

        self.assertNotContains(response, 'Shaltorin')
        self.assertNotContains(response, 'Falkrainne')


class EncounterAndInitiativeModelTest(TestCase):

    def test_save_initiative_object_and_retrieve(self):
        encounter_ = Encounter()
        encounter_.save()

        first_init = Initiative()
        first_init.creature_name = 'Shaltorin'
        first_init.initiative_value = 20
        first_init.encounter = encounter_
        first_init.save()

        second_init = Initiative()
        second_init.creature_name = 'Falkrainne'
        second_init.initiative_value = 2
        second_init.encounter = encounter_
        second_init.save()

        init_order = Initiative.objects.all()
        self.assertEqual(init_order.count(), 2)

        saved_encounter = Encounter.objects.first()
        self.assertEqual(saved_encounter, encounter_)

        first_saved_init = init_order[0]
        second_saved_init = init_order[1]

        self.assertEqual(first_saved_init, first_init)
        self.assertEqual(first_saved_init.encounter, encounter_)
        self.assertEqual(second_saved_init, second_init)
        self.assertEqual(second_saved_init.encounter, encounter_)