from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    PRODUCT_TILE = (By.CSS_SELECTOR,"[data-component-id='2']")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def product_select(self):
        e = self.driver.find_element(*self.PRODUCT_TILE)
        e.click()

