from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, '//div(@data-test="p=resultsCount"}')

    def verify_search_results(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert "tea" in actual_text, f'Error. Text tea not in {actual_text}'

