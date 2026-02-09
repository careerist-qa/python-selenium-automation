from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')


    def search(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(10)


    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)