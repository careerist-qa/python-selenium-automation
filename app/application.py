from pages.header import Header
from pages.main_page import MainPage
from pages.search_results import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.empty_cart_page import EmptyCartPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.empty_cart_page = EmptyCartPage(self.driver)

