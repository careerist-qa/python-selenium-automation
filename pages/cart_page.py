from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")
    CART_BTTN = (By.ID, 'nav-cart')

    def verify_empty_cart(self, string):
        self.verify_text(string, *self.EMPTY_CART)

    def click_cart(self):
        self.click(*self.CART_BTTN)
