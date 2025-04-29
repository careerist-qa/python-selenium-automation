from selenium.webdriver.common.by import By
from time import sleep
from Pages.base_page import BasePage

class Cart(BasePage):
    CART_ICON = By.CSS_SELECTOR,"div[data-test='@web/CartIcon']"
    MESSAGE = By.CSS_SELECTOR,"div[data-test='boxEmptyMsg']"
    PRODUCT_IN_CART = By.XPATH, "//span[text()='$6.69 subtotal']"

    def click_cart(self,*locator):
        self.click(*self.CART_ICON)
        sleep(5)

    def verify_message(self,*locator):
         self.find_element(*self.MESSAGE)

    def product_in_cart(self,*locator):
        self.find_element(*self.PRODUCT_IN_CART)






