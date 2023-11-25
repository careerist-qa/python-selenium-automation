from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGNIN_IN_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)  # wait for ads to disappear

    def hover_over_signin(self):
        signin_btn = self.find_element(*self.SIGNIN_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(signin_btn)
        actions.perform()

    def click_cart(self):
        self.wait_for_element_click(*self.CART_ICON)

    def verify_signin_arrow_shown(self):
        self.wait_for_element_visible(*self.SIGNIN_IN_ARROW)
