from selenium.webdriver.common.by import By

class CartPage:
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[contains(text(),'Your cart is empty')]")

    def __init__(self, driver):
        self.driver = driver

    def is_cart_empty_message_displayed(self):
        return self.driver.find_element(*self.EMPTY_CART_MESSAGE).is_displayed()
