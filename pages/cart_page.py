from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")

    def verify_product_name(self, part_name):
        self.verify_partial_text(part_name, *self.PRODUCT_NAME)