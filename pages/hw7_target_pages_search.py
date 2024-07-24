from pages.hw7_target_pages_base import Hw7PageBase
from selenium.webdriver.common.by import By
from time import sleep


class Hw7PageSearch(Hw7PageBase):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
    SEARCH_PRODUCT_TILE_S = (By.CSS_SELECTOR, '[data-test="product-title"]')

    def open_the_first_product_in_search_results(self):
        self.refresh_page()
        self.find_element(*self.SEARCH_PRODUCT_TILE_S).click()
