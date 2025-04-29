from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_RESULT=By.CSS_SELECTOR, "[data-test='resultsHeading']"

    def verify_search_results(self,product):
        actual_result = self.find_element(*self.SEARCH_RESULT).text
        assert product in actual_result, f'Expected result {product} not in {actual_result}'