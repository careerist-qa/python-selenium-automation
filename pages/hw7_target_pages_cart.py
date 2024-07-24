from selenium.webdriver.common.by import By
from pages.hw7_target_pages_base import Hw7PageBase

class Hw7PageCart(Hw7PageBase):
    CART_SUMMARY = (By.XPATH, '//span[contains(text(), "subtotal")]')
    CART_PRODUCT_TILE = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')

    def verify_cart_item_amount(self, amount):
        cart_summary = self.return_text_from_element(*self.CART_SUMMARY)
        assert f'{amount} item' in cart_summary, f'Expected "{amount} item" but got "{cart_summary}"'

    def verify_cart_item_tile(self, text):
        added_product_tile = text
        cart_product_tile = self.return_text_from_element(*self.CART_PRODUCT_TILE)
        assert added_product_tile[:20] == cart_product_tile[:20], f'Expected "{added_product_tile}" but got "{cart_product_tile}"'


