import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                cls.live_server_url = ''
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

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
        self.browser.get(self.server_url)

        # The page title reads 'Critaholic'
        self.assertIn('Critaholic', self.browser.title)

        # and gives a brief description of how to use it
        instruction_text = self.browser.find_element_by_id('instructions')
        self.assertIn('First, enter the name of the monster.', instruction_text.text)

        # She is invited to enter the name of a PC or monster and its initiative
        titles = self.browser.find_elements_by_tag_name('label')
        title_text = [title.text for title in titles]
        self.assertIn('Creature', title_text[0])
        self.assertIn('Initiative', title_text[1])
        self.assertIn('Starting HP', title_text[2])

        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')

        # She types in 'displacer beast' and '10'
        initiative_name_input.send_keys('Displacer beast')

        # find the input box for the initiative
        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')

        initiative_number_input.send_keys('10')

        # This displacer beast starts with 100 hit points, and she enters in that amount in the appropriate box
        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')

        initiative_number_input.send_keys('100')

        # Enter
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # When she hits enter the page updates and she sees a new, unique URL
        # the page displays the name of the displacer beast, the initiative number 10
        # and the hit point value 100

        # test the unique url?
        gina_init_url = self.browser.current_url
        self.assertRegex(gina_init_url, '/init/.+')

        self.check_for_cells_in_list_table('Displacer beast')
        self.check_for_cells_in_list_table('10')
        self.check_for_cells_in_list_table('100')

        # There is still a pair of text boxes ready to accept information
        # assert that the form fields are there
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')

        # She types in 'ettin
        initiative_name_input.send_keys('Ettin')

        # find the input box for the initiative
        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')

        # She types in '2', ettins not being known for their high dex
        initiative_number_input.send_keys('2')

        # This ettin starts with 125 hit points, and she enters in that amount in the appropriate box
        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')

        initiative_number_input.send_keys('125')

        # And she clicks 'submit'
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # And the page updates again, showing both creatures (sorted by initiative)
        # iterate through the cells and rows
        #    assert that the appropriate beasts are listed in the appropriate order

        self.check_for_cells_in_list_table('Displacer beast')
        self.check_for_cells_in_list_table('10')
        self.check_for_cells_in_list_table('100')
        self.check_for_cells_in_list_table('Ettin')
        self.check_for_cells_in_list_table('2')
        self.check_for_cells_in_list_table('125')

        # Gary the GM comes to the site too, having heard about the awesomeness
        self.browser.quit()
        self.browser = webdriver.Chrome('/Users/jd/Resources/chromedriver')
        self.browser.get(self.server_url)

        # He sees a brand new page, no sign of anyone else's encounter
        init_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Displacer beast', init_text)
        self.assertNotIn('Ettin', init_text)

        # Gary enters an monster
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')

        # He types in 'kobold'
        initiative_name_input.send_keys('Kobold')

        # find the input box for the initiative
        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')

        initiative_number_input.send_keys('1')

        # This kobold starts with 12 hit points, and he enters in that amount in the appropriate box
        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')

        initiative_number_input.send_keys('12')

        # Enter
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # the page refreshes and he gets his own url
        gary_init_url = self.browser.current_url
        self.assertRegex(gary_init_url, '/init/.+')
        self.assertNotEqual(gary_init_url, gina_init_url)

        # Gina's items are still not on the page, but Gary's are
        init_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Displacer beast', init_text)
        self.assertIn('Kobold', init_text)

    def test_user_can_modify_hit_point_values_on_existing_initiative_lines(self):
        # Gina starts another session, and navigates to critaholic
        self.browser.get(self.server_url)

        # she enters three creatures: two player characters and a monster
        # Kobold
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')

        initiative_name_input.send_keys('Kobold')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')

        initiative_number_input.send_keys('1')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')

        initiative_number_input.send_keys('12')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # Falkrainne
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')

        initiative_name_input.send_keys('Falkrainne')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')

        initiative_number_input.send_keys('15')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')

        initiative_number_input.send_keys('101')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # Shaltorin
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')

        initiative_name_input.send_keys('Shaltorin')

        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')

        initiative_number_input.send_keys('17')

        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')

        initiative_number_input.send_keys('120')

        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

        # Gina runs through the first round of combat and SURPRISE! the kobold is hit
        # She plugs the damage into the appropriate box and hits update

        kobold_hp_test = self.browser.find_element_by_id('Kobold_hp_display')
        self.assertEqual('12', kobold_hp_test.text)

        hp_input = self.browser.find_element_by_id('Kobold_hp_edit') # find hit points entry box
        hp_input.send_keys('4')
        hp_sub_button = self.browser.find_element_by_id('Kobold_hp_sub') # find button to subtract hp value
        hp_sub_button.click()

        kobold_hp_test = self.browser.find_element_by_id('Kobold_hp_display')
        self.assertEqual('8', kobold_hp_test.text)

        # Shaltorin's player decides that Falkrainne is doing poorly. He heals her for 12!
        falkrainne_hp_test = self.browser.find_element_by_id('Falkrainne_hp_display')
        self.assertEqual('101', falkrainne_hp_test.text)

        hp_input = self.browser.find_element_by_id('Falkrainne_hp_edit')  # find hit points entry box
        hp_input.send_keys('12')
        hp_add_button = self.browser.find_element_by_id('Falkrainne_hp_add')  # find button to subtract hp value
        hp_add_button.click()

        falkrainne_hp_test = self.browser.find_element_by_id('Falkrainne_hp_display')
        self.assertEqual('113', falkrainne_hp_test.text)

    def test_layout_and_styling_load(self):
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        instructions = self.browser.find_element_by_id('instructions')
        self.assertAlmostEqual(
            instructions.location['x'] + (instructions.size['width']/2),
            512,
            delta=5
        )

        # TODO form not robust, figure out default values and better error messaging
# todo add tests for redirect? or does that only belong in unit tests
# todo initiative entry behaviors: edit, reorder on edit, delete
# step: add notes field
# TODO long term goal: multiple authorized users can access and make adjustments to the same screen
# TODO The different characters and associated powers are listed along with targets. By selecting boxes and values,
#   such as 'Falkrainne', 'casts heal', 'Shaltorinn', the player can effect each other or monsters.
# todo encounter name/label?
# todo point to bootstrap service, not included min (necessary?)
# todo for list of initiative, \t or arrow or enter will highlight 'next' in turn order