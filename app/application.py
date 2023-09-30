from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.sign_in_page import SignInPage
from pages.base_page import Page



class Application:
    def __init__(self,driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.base_page  = Page(driver)

