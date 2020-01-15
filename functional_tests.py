from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# user hears about new online lists app
		# user goes to the homepage
		self.browser.get('http://localhost:8000')

		# user notices page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# User is invited to enter a to-do item straight away

		# User types "Buy peacock feathers" into a text box
		# (Her hobby is making fly fishing lures)

		# When she hits enter, the page updates, and now the page lists:
		# "1: Buy peacock feathers" an an item in a to-do list

		# There is still a text box inviting her to add another item
		# She enter "Use peacock feathers to make a fly"

		# The page updates again, and now shows both items on her list

		# User wonders whether the site will remember her list. 
		# Then, she sees that the site has generated a unique URL for her
		# there is some text explaining as much

		# She visits that URL - her to-do list is still there

		# Satisfied, she finishes with the app

if __name__ == '__main__':
	unittest.main(warnings='ignore')
