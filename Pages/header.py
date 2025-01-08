from selenium.webdriver import Keys

from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class HeaderPage(BasePage):

    SEARCH_BAR=By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']"
    SEARCH_BTN=By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"
    SIGN_IN_BUTTON = By.CSS_SELECTOR,"[aria-label='Account, sign in']"
    SIDE_NAV_SIGN_IN = By.CSS_SELECTOR,"[data-test='accountNav-signIn']"
    SIGN_IN_MESSAGE = By.CSS_SELECTOR, "//span[text()='Sign into your Target account']"

    def search_bar(self,product,*locator):
        self.input_text(product,*self.SEARCH_BAR).send_keys(product)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def sign_in(self,*locator):
        self.click(*self.SIGN_IN_BUTTON)
        sleep(5)

    def side_nav_sign_in(self,*locator):
        self.click(*self.SIDE_NAV_SIGN_IN)
        sleep(5)

    def verify_sign_in_page(self):
        self.verify_text('Sign into your Target account',*self.SIGN_IN_MESSAGE)


