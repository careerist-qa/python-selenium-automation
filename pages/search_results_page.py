from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, '//*[@id="', "")

    def verify_search_result(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULTS_HEADER)
        assert  expected_item == actual_text, f'Error: {expected_item} != {actual_text}'