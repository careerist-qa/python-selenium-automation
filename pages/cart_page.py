from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def verify_cart_empty_txt(self):
        self.verify_text('Your cart is empty', *self.HEADER)
