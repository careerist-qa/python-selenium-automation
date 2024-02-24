from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_TEXT}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # Dynamic locator
    def _get_header_locator(self, expected_header_text):
        # [By.XPATH, "//h1[text()=' Returns']"]
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_TEXT}', expected_header_text)]

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, help_topic):
        topics_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topics_dd)
        select.select_by_value(help_topic)

    def verify_returns_opened(self):
        self.wait_element_visible(*self.HEADER_RETURNS)

    def verify_promotions_opened(self):
        self.wait_element_visible(*self.HEADER_PROMOTIONS)

    def verify_header(self, expected_header_text):
        locator = self._get_header_locator(expected_header_text)
        print(locator)
        self.wait_element_visible(*locator)
