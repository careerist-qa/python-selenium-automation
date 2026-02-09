from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    def open_cart(self):
        self.open_url('https://www.target.com/cart')

    def verify_empty_cart(self):
        expected_result = 'Your cart is empty'
        actual_result = self.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
        assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
