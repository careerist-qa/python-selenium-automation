from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('tea', *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
