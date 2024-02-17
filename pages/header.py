from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_cart_icon(self):
        self.wait_element_clickable_click(*self.CART_ICON)
