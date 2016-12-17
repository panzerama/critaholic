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


class NewInitiativeTest(TestCase):

    def test_can_save_initiative_to_existing_list(self):
        other_encounter = Encounter.objects.create()
        this_encounter = Encounter.objects.create()

        self.client.post('/init/%d/add_init' % (this_encounter.id,),
                         data={'init_name': 'beholder', 'init_num': 18, 'init_hp': 150})

        self.assertEqual(Initiative.objects.count(), 1)
        new_init = Initiative.objects.first()
        self.assertEqual(new_init.creature_name, 'beholder')
        self.assertEqual(new_init.encounter, this_encounter)

    def test_new_initiative_redirects_after_POST(self):
        other_encounter = Encounter.objects.create()
        this_encounter = Encounter.objects.create()

        response = self.client.post('/init/%d/add_init' % (this_encounter.id,),
                                    data={'init_name': 'beholder', 'init_num': 18, 'init_hp': 150})

        self.assertRedirects(response, '/init/%d/' % (this_encounter.id,))


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
