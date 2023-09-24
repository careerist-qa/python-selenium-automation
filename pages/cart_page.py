from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")

    def verify_empty_cart(self):
        self.find_element(*self.EMPTY_CART)

