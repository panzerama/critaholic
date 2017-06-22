from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver import ActionChains as chain
from unittest import skip


class InitDragAndDrop(FunctionalTest):

    def add_initiative(self, name, initiative, hit_points):
        initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
        initiative_name_input.send_keys(name)
        initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
        initiative_number_input.send_keys(initiative)
        initiative_number_input = self.browser.find_element_by_id('initiative_hp_input')
        initiative_number_input.send_keys(hit_points)
        initiative_submit = self.browser.find_element_by_id('initiative_submit')
        initiative_submit.click()

    def create_list_of_initiative_entries(self):
        table = self.browser.find_element_by_id('init_table')
        cells = table.find_elements_by_id('initiative_name_display')
        return cells

    def test_drag_and_drop_reorders_elements(self):
        self.browser.get(self.server_url + '/init/')
        #Gina the GM needs to run a combat between two glorious heroes and a pack of evil goblins. She adds the Goblins
        #1, 2, 3, 4
        self.add_initiative("Goblin", 2, 10)
        self.add_initiative("Goblin", 3, 10)
        self.add_initiative("Goblin", 4, 10)
        self.add_initiative("Goblin", 5, 10)

        #and then adds the fearless heroes
        #Shaltorinn, Falkrainne
        self.add_initiative("Shaltorinn", 15, 150)
        self.add_initiative("Falkrainne", 17, 170)

        #test in-order, test order values?
        list_of_entries = self.create_list_of_initiative_entries()
        self.assertEqual(list_of_entries[0], 'Falkrainne')

        # When she's done entering, it's time to start the combat. Shaltorinn decides to screw things up by delaying his
        # action. Gina drags his initiative entry down one
        shaltorinn_entry = 0
        goblin_entry = 0
        drag_chain = chain(self)
        drag_chain.drag_and_drop()
        self.fail('finish the test')
        #But a goblin then delays after him, and she adjusts it again

    def test_drag_and_drop_order_preserved_on_reload(self):
        self.fail('write the drag and drop tests!')


