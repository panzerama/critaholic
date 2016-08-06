from django.core.urlresolvers import resolve
from django.test import TestCase
from initiative.views import home_page

class HomePageTest(TestCase):

	#TODO later on, change the home page to a menu system and move this to '/init'
	def test_root_url_resolves_to_initiative_tracker(self): 
		found = resolve('/')
		self.assertEqual(found.func, home_page)