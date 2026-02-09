from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage


class Application:


    def __init__(self, driver):


        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
