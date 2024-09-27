from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class HelpPage(Page):
    # HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    # HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER_TXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # Dynamic locator
    def _get_locator(self, expected_header_text):
        # (By.XPATH, "//h1[text()=' Returns']")
        # (By.XPATH, "//h1[text()=' {expected_header_text}']")
        # (By.XPATH, "//h1[text()=' {SUBSTRING}']") => (By.XPATH, "//h1[text()=' Current promotions']")
        return [self.HEADER_TXT[0], self.HEADER_TXT[1].replace('{SUBSTRING}', expected_header_text)]

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, option):
        dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(dd)
        select.select_by_value(option)

    def verify_header(self, expected_header_text):
        header_locator = self._get_locator(expected_header_text)
        self.wait_for_element_to_appear(*header_locator)

    # def verify_returns_opened(self):
    #     self.wait_for_element_to_appear(*self.HEADER_RETURNS)
    #
    # def verify_promotions_opened(self):
    #     self.wait_for_element_to_appear(*self.HEADER_PROMOTIONS)
