from selenium import webdriver
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
		self.fail('Finish the test!')

		# and gives a brief description of how to use it

		# She is invited to enter the name of a PC or monster and its initiative
		# She types in 'displacer beast' and '10'

		# When she hits enter the page updates and she sees 10 and the name of 
		# the displacer beast

		# There is still a pair of text boxes ready to accept information
		# Gina types in 'ettin' and '2'. She hits enter

		# And the page updates again, showing both creatures (though not sorted
		# by initiative)

		# Gina ends her session, but wonders if the site will remember this enc-
		# ounter's initiative order. She sees that the site has generated a uni-
		# que URL for her.

		# She visits that URL and, sure enough, the list is there, waiting for 
		# her.

		# Satisfied, she carries on with the session.

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
