from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def verify_cart_empty_message(self):
        self.wait_element_visible(*self.CART_HEADER)
        self.verify_text('Your cart is empty', *self.CART_HEADER)