from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

    def verify_cart_empty(self):
        expected_text='Your cart is empty'
        actual_text= self.driver.find_element(*self.CART_EMPTY_TXT).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'

    def verify_product_name(self,product):
        actual_name = self.driver.find_element(*self.CART_ITEM_TITLE).text
        assert product in actual_name, f'Expected {product} did not match actual {actual_name}'

    def verify_cart_items(self,amount):
        cart_summary = self.driver.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item in cart_summary, f"Expected {amount} items but got {cart_summary}'
