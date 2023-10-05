from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class ProductPage(Page):
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    PRODUCT_NAME = (By.ID, 'productTitle')

    def open_product(self,*product_id):
            self.driver.get(f'https://www.amazon.com/dp/{product_id}/')
            sleep(2)
            self.driver.refresh()

    def product_name_get(self):
        p = self.driver.find_element(*self.PRODUCT_NAME).text[:30]
        print(f'Current product: {p}')

    def product_add_to_cart(self):
        e = self.driver.find_element(*self.ADD_TO_CART)
        e.click()
        print('Product added')



    def verify_can_click_colors(self):
        pass


