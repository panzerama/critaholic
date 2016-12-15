from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.test import TestCase
from django.http import HttpRequest
from initiative.views import home_page
# from django.views.decorators.csrf import csrf_exempt
from initiative.models import Initiative


class HomePageTest(TestCase):

    # TODO later on, change the home page to a menu system and move this to '/init'
    def test_root_url_resolves_to_initiative_tracker(self): 
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # testing csrf tokens is difficult in 1.10, testing only a part of the pages
    def test_home_page_shows_correct_html(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['init_name'] = 'beholder'
        request.POST['init_num'] = 18
        response = home_page(request)
        expected_output = render(request, 'home.html')
        self.assertEqual(response.content.decode()[:40], expected_output.content.decode()[:40])

    # fix the lack of CSRF testing by implementing django.test.Client?
    def test_name_and_init_input_saved_by_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['init_name'] = 'beholder'
        request.POST['init_num'] = 18
        response = home_page(request)

        self.assertEqual(Initiative.objects.count(), 1)
        new_init_order = Initiative.objects.first()
        self.assertEqual(new_init_order.creature_name, 'beholder')
        self.assertEqual(new_init_order.initiative_value, 18)

        self.assertIn('beholder', response.content.decode())
        self.assertIn('18', response.content.decode())

    def test_home_page_displays_all_monsters_in_order(self):
        Initiative.objects.create(creature_name='beholder', initiative_value=10)
        Initiative.objects.create(creature_name='displacer beast', initiative_value=11)

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('beholder', response.content.decode())
        self.assertIn('10', response.content.decode())
        self.assertIn('displacer beast', response.content.decode())
        self.assertIn('11', response.content.decode())


class ItemModelTest(TestCase):

    def test_save_initiative_object_and_retrieve(self):
        first_init = Initiative()
        first_init.creature_name = 'Shaltorin'
        first_init.initiative_value = 1
        first_init.save()

        second_init = Initiative()
        second_init.creature_name = 'Falkrainne'
        second_init.initiative_value = 20
        second_init.save()

        init_order = Initiative.objects.all()
        self.assertEqual(init_order.count(), 2)

        first_saved_init = init_order[0]
        second_saved_init = init_order[1]

        self.assertEqual(first_saved_init, first_init)
        self.assertEqual(second_saved_init, second_init)