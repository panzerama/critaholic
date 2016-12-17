from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/jd/Resources/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_cells_in_list_table(self, cell_text):
        table = self.browser.find_element_by_id('init_table')
        cells = table.find_elements_by_tag_name('td')
        self.assertIn(cell_text, [cell.text for cell in cells])

    def test_new_user_can_create_initiative(self):
        # Gina the GM has heard about a fantastic new app for tracking 
        # initiative. She decides to try it out. She opens a browser and 
        # navigates to the page.
        self.browser.get(self.live_server_url)

        # The page title reads 'Critaholic'
        self.assertIn('Critaholic', self.browser.title)

        # and gives a brief description of how to use it
        instruction_text = self.browser.find_element_by_id('instructions')
        self.assertIn('First, enter the name of the monster.', instruction_text.text)
        self.assertIn('Second, enter the initiative.', instruction_text.text)

        # She is invited to enter the name of a PC or monster and its initiative
        # TODO for titles for name, initiative, hit points
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        self.assertEqual(
            initiative_name_input.get_attribute('placeholder'),
            'Enter a monster\'s name'
        )

        # She types in 'displacer beast' and '10'
        initiative_name_input.send_keys('Displacer beast')

        # find the input box for the initiative
        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        self.assertEqual(
            initiative_number_input.get_attribute('placeholder'),
            'Enter the monster\'s initiative'
        )
        initiative_number_input.send_keys('10')

        # This displacer beast starts with 100 hit points, and she enters in that amount in the appropriate box
        # TODO test for hp box

        # Enter
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # When she hits enter the page updates and she sees a new, unique URL
        # the page displays the name of the displacer beast, the initiative number 10
        # and the hit point value 100
        # TODO test for hp value

        # test the unique url?
        gina_init_url = self.browser.current_url
        self.assertRegex(gina_init_url, '/init/.+')

        self.check_for_cells_in_list_table('Displacer beast')
        self.check_for_cells_in_list_table('10')

        # There is still a pair of text boxes ready to accept information
        # assert that the form fields are there
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        self.assertEqual(
            initiative_name_input.get_attribute('placeholder'),
            'Enter a monster\'s name'
        )

        # She types in 'ettin
        initiative_name_input.send_keys('Ettin')

        # find the input box for the initiative
        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        self.assertEqual(
            initiative_number_input.get_attribute('placeholder'),
            'Enter the monster\'s initiative'
        )

        # She types in '2', ettins not being known for their high dex
        initiative_number_input.send_keys('2')

        # TODO add test for entering second hp value

        # And she clicks 'submit'
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # And the page updates again, showing both creatures (sorted by initiative)
        # iterate through the cells and rows
        #    assert that the appropriate beasts are listed in the appropriate order

        self.check_for_cells_in_list_table('Displacer beast')
        self.check_for_cells_in_list_table('10')
        self.check_for_cells_in_list_table('Ettin')
        self.check_for_cells_in_list_table('2')

        # Gina runs through the first round of combat and SURPRISE! the ettin is hit
        # She plugs the damage into the appropriate box and hits update
        # TODO put negative value in box
        # the amount is removed from the hp total for that creature.
        # TODO click submit
        # TODO check that the amount updated correctly
        # TODO put positive value in box
        # TODO click submit
        # TODO check that the amount updated correctly

        # Gary the GM comes to the site too, having heard about the awesomeness
        self.browser.quit()
        self.browser = webdriver.Chrome('/Users/jd/Resources/chromedriver')
        self.browser.get(self.live_server_url)

        # He sees a brand new page, no sign of anyone else's encounter
        init_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Displacer beast', init_text)
        self.assertNotIn('Ettin', init_text)

        # Gary enters an monster
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        self.assertEqual(
            initiative_name_input.get_attribute('placeholder'),
            'Enter a monster\'s name'
        )

        # He types in 'kobold'
        initiative_name_input.send_keys('Kobold')

        # find the input box for the initiative
        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        self.assertEqual(
            initiative_number_input.get_attribute('placeholder'),
            'Enter the monster\'s initiative'
        )
        initiative_number_input.send_keys('1')

        # TODO hit point entry

        # Enter
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # the page refreshes and he gets his own url
        gary_init_url = self.browser.current_url
        self.assertRegex(gary_init_url, '/init/.+')
        self.assertNotEqual(gary_init_url, gina_init_url)

        # Gina's items are still not on the page, but Gary's are
        # TODO add checks for hit point values
        init_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Displacer beast', init_text)
        self.assertIn('Kobold', init_text)

# next step: initiative entry behaviors: edit, reorder on edit, delete
# step: add hit points fields
# step: add notes field
