from .base import FunctionalTest


class HomePageTest(FunctionalTest):

    def search_page_links(self):
        page_links = self.browser.find_elements_by_tag_name('a')


    def test_home_page_presents_correct_apps(self):
        # gina navigates to critaholic.com and finds, when the page loads, the expected page title
        self.browser.get(self.server_url)
        self.assertIn('Critaholic', self.browser.title)

        # compare text of introduction id to expected
        introduction = self.browser.find_element_by_id('introduction')
        self.assertIn('a suite of tools for DM\'s', introduction.text)

        # after she reads the introduction, she sees a list of options for different apps


        #update this list as new apps are created


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

        self.fail('write the future tests')
        # Future changes:
        # make sure the links to various apps are modified by class when they have been visited?
        # somehow check if animations or classes are displayed correctly?
        # expand to check that all of the options are there
