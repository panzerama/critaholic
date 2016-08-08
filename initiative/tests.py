from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.test import TestCase
from django.http import HttpRequest
from initiative.views import home_page
from django.views.decorators.csrf import csrf_exempt

class HomePageTest(TestCase):

	#TODO later on, change the home page to a menu system and move this to '/init'
	def test_root_url_resolves_to_initiative_tracker(self): 
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_shows_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_output = render(request, 'home.html')
		self.assertEqual(response.content.decode(), expected_output.content.decode())

	def test_name_and_init_input_saved_by_POST(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['init_name'] = 'beholder'
		request.POST['init_num'] = '18'
		response = home_page(request)

		expected_html = render(request, 'home.html', {'init_name_text': 'beholder', 'init_num_text': '18'})
		self.assertEqual(response.content.decode(), expected_html.content.decode())

# todo go back and find a way to test csrf tokens, ffs
