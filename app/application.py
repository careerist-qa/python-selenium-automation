from pages.base_page import Page
from pages.cart_page import Cart_Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:
    def __init__(self, driver):
        self.cart_page = Cart_Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.page = Page(driver)
        self.search_results_page = SearchResultsPage(driver)