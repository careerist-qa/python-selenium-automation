from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)