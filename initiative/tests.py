from django.test import TestCase
from django.http import HttpRequest
from initiative.views import home_page

class HomePageTest(TestCase):
    def test_home_page_displays_initiative_tracker(self):
        # Arrange & Act
        response = self.client.get("/")

        # Assert
        self.assertContains(response, "<title>Initiative Tracker</title>")
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")
