from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_returns_opened(self):
        self.wait_for_element_appear(*self.HEADER_RETURNS)

    def select_topic(self, help_topic):
        topic_selection = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_selection)
        select.select_by_value(help_topic)

    def verify_promotions_opened(self):
        self.wait_for_element_appear(*self.HEADER_PROMOTIONS)
