from .base import FunctionalTest
from selenium import webdriver
from unittest import skip


class NewCharacterTest(FunctionalTest):

    def test_new_user_can_create_character(self):
        # Gina the GM has heard about a fantastic new app for tracking 
        # her character notes. She decides to try it out. She opens a browser and
        # navigates to the page.
        self.browser.get(self.server_url + '/character/')

        # The page title reads 'Critaholic: Character'
        self.assertIn('Critaholic: Character', self.browser.title)

        # and gives a brief description of how to use it
        instruction_text = self.browser.find_element_by_id('instructions')
        self.assertIn('First, enter your character\'s name.', instruction_text.text)

        # She is invited to enter the name of a character
        self.fail("Continue the user story!")
