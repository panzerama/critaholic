from .base import FunctionalTest
from selenium import webdriver
from unittest import skip


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling_load(self):
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        instructions = self.browser.find_element_by_id('instructions')
        self.assertAlmostEqual(
            instructions.location['x'] + (instructions.size['width']/2),
            512,
            delta=5
        )
