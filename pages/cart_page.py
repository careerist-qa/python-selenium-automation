from selenium.webdriver.common.by import By

from pages.base_page import Page


class Cart_Page(Page):
    EMPTY_CART_MESSAGE = (By.XPATH, "//h1[contains(@class, styles_ndsHeading)]")

    def verify_empty_cart_message(self):
        actual_text = self.find_element(*self.EMPTY_CART_MESSAGE).text
        assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text not in {actual_text}"


