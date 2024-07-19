from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    
    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'coffee' in actual_text, f'Expected coffee not in actual {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'coffee' in url, f'Expected "coffee" not in {url}'