from selenium.webdriver.common.by import By
from pages.base_page import Page
from behave import given, when, then


class CartPage(Page):
    Empty_Cart = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')

    def verify_your_shopping_cart_is_empty_text_present(self):
     self.driver.find_element(*self.Empty_Cart)