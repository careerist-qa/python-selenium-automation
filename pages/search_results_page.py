from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")

    def verify_search_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT_TXT)

    def verify_search_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)
