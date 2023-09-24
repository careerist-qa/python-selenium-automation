from pages.main_page import MainPage
from pages.signin_page import SigninPage
from pages.header import Header
from pages.base_page import Page
from pages.cart_page import CartPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.signin_page = SigninPage(driver)
        self.header = Header(driver)
        self.cart_page = CartPage(driver)
