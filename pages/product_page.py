from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text