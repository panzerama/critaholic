from .base import FunctionalTest
from selenium import webdriver
from unittest import skip


class FormValidationTest(FunctionalTest):

    def test_cannot_add_empty_initiative(self):
        # Gina goes to the home page and accidentally tries to submit an empty initiative item.
        self.browser.get(self.server_url)

        # confirm the fields are there
        titles = self.browser.find_elements_by_tag_name('label')
        title_text = [title.text for title in titles]
        self.assertIn('Creature', title_text[0])
        self.assertIn('Initiative', title_text[1])
        self.assertIn('Starting HP', title_text[2])

        # She hits Enter on the empty input box
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # The home page refreshes, and there is an error message saying that initiative items cannot be blank
        error_message = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error_message.text, "An initiative entry must have a name!")

        # She tries again with some text for the initiative, which now works
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys('Displacer beast')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys('100')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # She receives a similar warning on the encounter page
        error_message = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error_message.text, "An initiative entry must have an initiative value")

        # And she can correct it by filling some text in
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys('Displacer beast')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        initiative_number_input.send_keys('10')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys('100')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        gina_init_url = self.browser.current_url
        self.assertRegex(gina_init_url, '/init/.+')

        self.check_for_cells_in_list_table('Displacer beast')
        self.check_for_cells_in_list_table('10')
        self.check_for_cells_in_list_table('100')