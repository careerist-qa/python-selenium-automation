from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class ChipsPage(BasePage):

    ADD_TO_CART_ON_CHIPS_PAGE = By.CSS_SELECTOR, "[aria-label='Add Doritos Nacho Cheese Flavor Party Size Tortilla Chips - 14.5oz to cart']"

def click_add_to_cart(self ,*locator):
    self.click(*self.ADD_TO_CART_ON_CHIPS_PAGE)