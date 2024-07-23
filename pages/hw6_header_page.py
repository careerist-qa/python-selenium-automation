from selenium.webdriver.common.by import By
from pages.hw6_base_page import Hw6Page


class Hw6HeaderPage(Hw6Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')
    CART_BUTTON = (By.CSS_SELECTOR, 'div[data-test="@web/CartIcon"]')

    def search(self):
        self.input_text('coffee', *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)

    def cart_click(self):
        self.click(*self.CART_BUTTON)


