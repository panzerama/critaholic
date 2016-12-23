import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from unittest import skip


class FunctionalTest(StaticLiveServerTestCase):

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
