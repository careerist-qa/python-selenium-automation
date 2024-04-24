from  pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage


class Application:
    def __init__(self, driver):
        self.main = MainPage(driver)
        self.header = Header(driver)
        self.search_results = SearchResultsPage(driver)