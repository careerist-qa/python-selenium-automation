from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_TXT)
