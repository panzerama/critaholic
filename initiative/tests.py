from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from initiative.views import home_page

class HomePageTest(TestCase):

	#TODO later on, change the home page to a menu system and move this to '/init'
	def test_root_url_resolves_to_initiative_tracker(self): 
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_shows_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_output = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_output)



#my guesses as to the next tests before reading on
# home page renders the how-to text
# home page renders the form fields
# home page renders default text
# entering information in the fields and pressing enter refreshes the page
# information from a request is returned properly in response