from selenium.webdriver.common.by import By
from pages.hw6_base_page import Hw6Page


class Hw6SearchResultPage(Hw6Page):
    SEARCH_RESULTS_TEXT = (By.CSS_SELECTOR, '[data-test="resultsHeading"]')

    def verify_text(self):
        actual_test = self.driver.find_element(*self.SEARCH_RESULTS_TEXT)
        assert 'coffee' in actual_test.text, f'Expected coffee but got {actual_test.text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'coffee' in url, f'Expected coffee but got {url}'
