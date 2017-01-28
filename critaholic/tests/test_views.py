from django.core.urlresolvers import resolve
from django.test import TestCase
from critaholic.views import home_page


class HomePageTest(TestCase):

    def test_root_url_uses_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_base_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base_home.html')