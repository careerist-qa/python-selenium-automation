from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results_correct(self, expected_result):
        self.verify_partial_text(expected_result, *self.SEARCH_RESULTS_HEADER)

    def verify_search_results_page_url(self, expected_part_url):
        self.verify_partial_url(expected_part_url)
