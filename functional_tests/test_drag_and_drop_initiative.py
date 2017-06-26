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
        cells = table.find_elements_by_class_name('initiative_name_display')
        return [cell.text for cell in cells]

    def test_drag_and_drop_reorders_elements(self):
        self.browser.get(self.server_url + '/init/')
        #Gina the GM needs to run a combat between our glorious hero and an evil goblin. She adds the Goblin
        self.add_initiative("Goblin", 2, 10)

        #and then adds the fearless hero
        self.add_initiative("Shaltorinn", 15, 150)

        #test in-order, test order values?
        list_of_entries = self.create_list_of_initiative_entries()
        self.assertEqual(list_of_entries[0], 'Shaltorinn')

        # When she's done entering, it's time to start the combat. Shaltorinn decides to screw things up by delaying his
        # action. Gina drags his initiative entry down one
        shaltorinn_entry = self.browser.find_elements_by_xpath('//div[contains(text(), "Shaltorinn")]')
        goblin_entry = self.browser.find_elements_by_xpath('//div[contains(text(), "Goblin")]')
        drag_chain = chain(self.browser)
        drag_chain.drag_and_drop(shaltorinn_entry, goblin_entry)
        drag_chain.perform()

        init_first_in_order = self.browser.find_element_by_id('name1')

        self.assertEqual(init_first_in_order.text, 'Goblin')

        #But a goblin then delays after him, and she adjusts it again
        shaltorinn_entry = self.browser.find_elements_by_xpath('//div[contains(text(), "Shaltorinn")]')
        goblin_entry = self.browser.find_elements_by_xpath('//div[contains(text(), "Goblin")]')
        drag_chain = chain(self.browser)
        drag_chain.drag_and_drop(goblin_entry, shaltorinn_entry)
        drag_chain.perform()

        init_first_in_order = self.browser.find_element_by_id('name1')

        self.assertEqual(init_first_in_order.text, 'Shaltorinn')

        #She seems satisfied with her encounter

    def test_drag_and_drop_order_preserved_on_reload(self):
        self.fail('write the second set of drag and drop tests!')


