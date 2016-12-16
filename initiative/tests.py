from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.test import TestCase
from django.http import HttpRequest
from initiative.views import home_page
# from django.views.decorators.csrf import csrf_exempt
from initiative.models import Initiative


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
        self.assertEqual(response['location'], '/init/the-only-encounter-in-the-world/')


class InitViewTest(TestCase):

    def test_uses_init_view_template(self):
        response = self.client.get('/init/the-only-encounter-in-the-world/')
        self.assertTemplateUsed(response, 'init_view.html')

    def test_displays_all_monsters_in_order(self):
        Initiative.objects.create(creature_name='beholder', initiative_value=10)
        Initiative.objects.create(creature_name='displacer beast', initiative_value=11)

        response = self.client.get('/init/the-only-encounter-in-the-world/')

        self.assertContains(response, 'beholder')
        self.assertContains(response, '10')
        self.assertContains(response, 'displacer beast')
        self.assertContains(response, '11')


class ItemModelTest(TestCase):

    def test_save_initiative_object_and_retrieve(self):
        first_init = Initiative()
        first_init.creature_name = 'Shaltorin'
        first_init.initiative_value = 20
        first_init.save()

        second_init = Initiative()
        second_init.creature_name = 'Falkrainne'
        second_init.initiative_value = 2
        second_init.save()

        init_order = Initiative.objects.all()
        self.assertEqual(init_order.count(), 2)

        first_saved_init = init_order[0]
        second_saved_init = init_order[1]

        self.assertEqual(first_saved_init, first_init)
        self.assertEqual(second_saved_init, second_init)