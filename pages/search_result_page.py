from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')

    def verify_search_result(self, result):  # "tea"
        self.verify_text(result, *self.SEARCH_RESULT)