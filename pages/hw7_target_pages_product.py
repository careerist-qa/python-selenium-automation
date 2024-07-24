from pages.hw7_target_pages_base import Hw7PageBase
from selenium.webdriver.common.by import By


class Hw7PageProduct(Hw7PageBase):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
    SEARCH_PRODUCT_TILE_P = (By.CSS_SELECTOR, 'h1[data-test="product-title"]')
    VIEW_CART_CHECKOUT = (By.CSS_SELECTOR, '[href="/cart"]')

    def save_the_product_title(self):
        added_product_title = self.return_text_from_element(*self.SEARCH_PRODUCT_TILE_P)
        return added_product_title

    def add_the_product_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BUTTON).click()

    def view_cart_and_checkout(self):
        self.find_element(*self.VIEW_CART_CHECKOUT).click()
