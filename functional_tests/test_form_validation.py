from .base import FunctionalTest
# from selenium import webdriver
from unittest import skip


class FormValidationTest(FunctionalTest):

    @skip("skipped form validation")
    def test_cannot_add_empty_initiative(self):
        # Gina goes to the home page and accidentally tries to submit an empty initiative item.
        self.browser.get(self.server_url)

        # confirm the fields are there
        titles = self.browser.find_elements_by_tag_name('label')
        title_text = [title.text for title in titles]
        self.assertIn('Creature', title_text[0])
        self.assertIn('Initiative', title_text[1])
        self.assertIn('Starting HP', title_text[2])

        # She hits Enter without filling in the name field
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys('')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        initiative_number_input.send_keys('10')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys('100')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # The home page refreshes, and there is an error message saying that initiative items cannot be blank
        error_message = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error_message.text, "An initiative entry must have a name!")

        # The second time she does it the right way
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys('Displacer Beast')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        initiative_number_input.send_keys('10')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys('100')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # And it checks out as working
        self.check_for_cells_in_list_table('Displacer Beast')
        self.check_for_cells_in_list_table('10')
        self.check_for_cells_in_list_table('100')

        # For some perverse reason, she does it again.
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys('')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        initiative_number_input.send_keys('6')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys('80')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # Sure enough, this produces a warning
        error_message = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error_message.text, "An initiative entry must have a name!")

        # She tries it one more time
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys('Young Dragon')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        initiative_number_input.send_keys('6')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys('80')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # And it checks out as working
        self.check_for_cells_in_list_table('Young Dragon')
        self.check_for_cells_in_list_table('6')
        self.check_for_cells_in_list_table('80')

        # Finally, she hits Enter without filling in the number field
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys('Falkrainne')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        initiative_number_input.send_keys('')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys('134')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # The home page refreshes, and there is an error message saying that initiative items cannot be blank
        error_message = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error_message.text, "An initiative entry must have a valid initiative value!")