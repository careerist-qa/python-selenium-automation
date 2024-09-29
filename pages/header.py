from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    NAV_SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load

    def click_cart(self):
        self.click(*self.CART_BTN)
       # self.driver.find_element(*self.CART_BTN).click()

    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def click_right_side_nav_sign_in(self):
        self.click(*self.NAV_SIGN_IN)