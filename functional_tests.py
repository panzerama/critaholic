from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_new_user_can_create_initiative(self):

		# Gina the GM has heard about a fantastic new app for tracking 
		# initiative. She decides to try it out. She opens a browser and 
		# navigates to the page.
		self.browser.get('http://localhost:8000')

		# The page title reads 'Critaholic'
		self.assertIn('Critaholic', self.browser.title)

		# and gives a brief description of how to use it
		instruction_text = self.browser.find_element_by_id('instructions')
		self.assertIn('First, enter the name of the monster.', instruction_text)
		self.assertIn('Second, enter the initiative.', instruction_text)

		# She is invited to enter the name of a PC or monster and its initiative
		# She types in 'displacer beast' and '10'
		# find the input box for monster name
		initiative_name_input = self.browser.find_element_by_id('initiative_name_input')
		initiative_name_input.send_keys('Displacer beast')
		# find the input box for the initiative
		initiative_number_input = self.browser.find_element_by_id('initiative_number_input')
		initiative_number_input.send_keys('10')
		# Enter 
		initiative_number_input.send_keys(Keys.ENTER)

		# When she hits enter the page updates and she sees 10 and the name of 
		# the displacer beast
		# assert that the words displacer beast and the number ten are in 
		# a row or cell that match the right id.
		name_display_cells = self.browser.find_elements_by_name('initiative_name_display')
		init_display_cells = self.browser.find_elements_by_name('initiative_number_display')
		self.assertTrue(any(name_display_cells.text == 'Displacer Beast'))
		self.assertTrue(any(init_display_cells.text == '10'))
		self.fail('Finish the test!')

		# There is still a pair of text boxes ready to accept information
		# assert that the form fields are there

		# Gina types in 'ettin' and '2'. She hits enter
		# send keys again


		# And the page updates again, showing both creatures (sorted by initiative)
		# iterate through the cells and rows
		#	assert that the appropriate beasts are listed in the appropriate order


		# Gina ends her session, but wonders if the site will remember this enc-
		# ounter's initiative order. She sees that the site has generated a uni-
		# que URL for her.
		# assert something about the url

		# She visits that URL and, sure enough, the list is there, waiting for 
		# her.
		# browser gets the unique url
		# test that the things we expect are displayed

		# Satisfied, she carries on with the session.
		# end test one.

		# Second tier project goals
		# 	Add hit points to the monsters
		#	Let the user change the hit points
		# 	Automatically sort the list
		#	Delete monsters
		# Third tier project goals
		#	drag and drop items to reorganize
		#	create multiple monsters
		# Future
		# 	Mobile responsive design
		# Other projects
		#	an app for tracking distances between creatures

if __name__ == '__main__':
	unittest.main()
