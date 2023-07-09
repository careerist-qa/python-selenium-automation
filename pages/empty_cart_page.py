from selenium.webdriver.common.by import By
from pages.base_page import Page


class EmptyCartPage(Page):
    CART_BTN = (By.ID, "nav-cart")
    EMPTY_CART_MESSAGE = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]")

    def verify_empty_cart(self):
        self.driver.find_element(*self.CART_BTN).click()
        self.driver.find_element(*self.EMPTY_CART_MESSAGE)

    # def click_cart_button(self):
    #     self.driver.find_element(*self.CART_BTN).click()
    #
    # def verify_empty_cart(self):
    #     self.driver.find_element(*self.EMPTY_CART_MESSAGE)
