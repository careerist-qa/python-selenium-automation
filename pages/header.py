from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGNIN_IN_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_cart_icon(self):
        self.wait_element_clickable_click(*self.CART_ICON)

    def hover_signin_btn(self):
        sign_in_btn = self.find_element(*self.SIGNIN_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(sign_in_btn)
        actions.perform()

    def verify_signin_arrow(self):
        self.wait_element_visible(*self.SIGNIN_IN_ARROW)