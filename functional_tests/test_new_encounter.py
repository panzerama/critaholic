from .base import FunctionalTest
from selenium import webdriver
from unittest import skip


class FormValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_initiative(self):
        # Gina goes to the home page and accidentally tries to submit an empty initiative item.
        # She hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying that initiative items cannot be blank

        # She tries again with some text for the initiative, which now works

        # Perversely, she now decides to submit a second blank initiative

        # She receives a similar warning on the encounter page

        # And she can correct it by filling some text in
        self.fail('write me!')