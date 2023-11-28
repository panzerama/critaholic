from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest

class NewInitiativeTest(unittest.TestCase):
    def setUp(self):
        # Arrange, run before the tests every time
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # A common test framework feature, you should think of this as part of the Arrange step, its logical end
        self.browser.quit()
    
    def test_can_start_initiative_session(self):
        # Alice is about to start a session for her D&D group
        # She goes to Critaholic to start an initiative tracker
        self.browser.get("http://localhost:8000/")

        # She sees 'Critaholic' in the browser title - Assert
        self.assertIn("Critaholic", self.browser.title)

        # And a header for the initiative tracker
        initiative_tracker_header = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertIn("Initiative Tracker", initiative_tracker_header.text)

        # There's a text box waiting for her to enter a character name and initiative value
        init_name_input_box = self.browser.find_element(By.ID, "new_initiative_name")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Character or NPC name")
        init_value_input_box = self.browser.find_element(By.ID, "new_initiative_value")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Initiative value")

        # After typing in the name and number she hits enter
        init_name_input_box.send_keys("Falkrainne")
        init_value_input_box.send_keys("20")
        init_value_input_box.send_keys(Keys.ENTER) # make this a click action instead
        time.sleep(1)

        # And sees that name and number in the table
        table = self.browser.find_element(By.ID, "intitiative_table")
        rows = table.find_elements(By.TAG_NAME, "tr")  
        self.assertTrue(any(row.text == "20: Falkrainne" for row in rows))

        # We're not done till the feature is done!
        self.fail("Finish the feature test!")

if __name__ == "__main__":
    unittest.main()