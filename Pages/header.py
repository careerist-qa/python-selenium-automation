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
    CATEGORIES_BTN =By.CSS_SELECTOR,"[aria-label='Categories']"
    GROCERY_BTN = By.CSS_SELECTOR,"[data-url='/c/grocery/-/N-5xt1a']"
    SNACK_BTN = By.CSS_SELECTOR,"[data-url='/c/snacks-grocery/-/N-5xsy9']"
    CHIPS_BTN = By.CSS_SELECTOR, "[data-url='/c/chips-snacks-grocery/-/N-5xsy7']"
    ADD_TO_CART_SIDE_NAV_PAGE = By.CSS_SELECTOR, "[data-test='orderPickupButton']"
    VIEW_CART = By.CSS_SELECTOR, "[href='/cart']"

    def click_category(self,*locator):
        self.click(*self.CATEGORIES_BTN)


    def click_grocery(self,*locator):
        self.click(*self.GROCERY_BTN)


    def click_snacks(self,*locator):
        self.click(*self.SNACK_BTN)


    def click_chips(self,*locator):
        self.click(*self.CHIPS_BTN)


    def click_add_to_side(self,*locator):
        self.click(*self.ADD_TO_CART_SIDE_NAV_PAGE)


    def click_view_cart(self,*locator):
        self.click(*self.VIEW_CART)


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


    def verify_sign_in_page(self,expected_text,*locator):
        self.verify_text('Sign into your Target account',*self.SIGN_IN_MESSAGE)





