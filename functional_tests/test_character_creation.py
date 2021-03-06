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
        character_name_input = self.browser.find_element_by_id('character_name_input')

        # She types in 'displacer beast' and '10'
        character_name_input.send_keys('Nils \"Carver\" Dacke')

        # And asked to enter a short description
        character_description_input = self.browser.find_element_by_id('character_description_input')

        # She types in 'displacer beast' and '10'
        character_description_input.send_keys('A murderous rogue with delusions of infamy.')

        # That done, she clicks on submit
        character_submit = self.browser.find_element_by_id('character_submit')
        character_submit.click()

        # and the page refreshes to a view of the character
        character_name = self.browser.find_element_by_id('character_name')
        self.assertEqual(character_name.text, 'Nils \"Carver\" Dacke')

        character_description = self.browser.find_element_by_id('character_description')
        self.assertEqual(character_description.text, 'A murderous rogue with delusions of infamy.')

        self.fail("Continue the user story!")

