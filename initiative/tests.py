from django.test import TestCase
from django.http import HttpRequest
from initiative.views import home_page

class HomePageTest(TestCase):
    def test_home_page_displays_initiative_tracker(self):
        # Arrange
        request = HttpRequest()

        # Act
        response = home_page(request)
        html = response.content.decode("utf-8")

        # Assert
        self.assertIn("<title>Initiative Tracker</title>", html)