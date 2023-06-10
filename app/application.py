from pages.header import Header
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_results import SearchResultsPage
from pages.signin_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.cart_page = CartPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
