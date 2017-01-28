from .base import FunctionalTest


class HomePageTest(FunctionalTest):

    def test_home_page_presents_correct_apps(self):
        # gina navigates to critaholic.com and finds, when the page loads, a brief introduction to the site
        self.browser.get(self.server_url)

        # compare text of introduction id to expected
        introduction = self.browser.find_element_by_id('introduction')
        self.assertContains(introduction.text, 'a suite of tools for DM\'s')

        # after she reads the introduction, she sees a list of options for different apps
        link_pasta = self.browser.find_elements_by_class_name('app-links')

        #update this list as new apps are created
        expected_links = ['Initiative', 'Character']
        for link in link_pasta:
            self.assertIn(link.text, expected_links)

        # for each link with the appropriate class, confirm text and link direction
        # she chooses to navigate to the Initiative app
        initiative_link = self.browser.find_element_by_link_text('whatever the link is')
        initiative_link.click()

        # regex test url
        destination_url = self.browser.current_url
        self.assertRegex(destination_url, '/init/.+')

        # when the page loads, she changes her mind, and returns to the front page, seeing the same change
        # select home link from Critaholic banner
        home_link = self.browser.find_element_by_id('banner_link')
        home_link.click()


        # Future changes:
        # make sure the links to various apps are modified by class when they have been visited?
        # somehow check if animations or classes are displayed correctly?
        # expand to check that all of the options are there
        self.fail("write the tests")
