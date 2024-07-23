from pages.hw6_base_page import Hw6Page
from selenium.webdriver.common.by import By


class Hw6CartPage(Hw6Page):
    EMPTY_CART_CONTAINER = (By.CSS_SELECTOR, '[data-test="emptyCartContainer"] h1')

    def verify_empty_message_equal(self):
        expected_message = 'Your cart is empty'
        actual_message = self.find_element(*self.EMPTY_CART_CONTAINER).text
        assert expected_message == actual_message, f'Expected "{expected_message}" but got "{actual_message}"'

    def verify_empty_message_contain(self):
        expected_message = 'empty'
        actual_message = self.find_element(*self.EMPTY_CART_CONTAINER).text
        assert expected_message in actual_message, f'Expected "{expected_message}" but not in "{actual_message}"'