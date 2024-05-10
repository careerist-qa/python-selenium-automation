from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignIn


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultsPage(driver)
        self.sign_in_page = SignIn(driver)
        self.pages = Page(driver)





