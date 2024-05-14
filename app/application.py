from pages.base_page import Page
from pages.bestsellers_page import BestsellersPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.target_help_page import TargetHelpPage
from pages.target_sign_in import TargetSignIn


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.bestsellers_page = BestsellersPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.base_page = Page(self.driver)
        self.target_help_page = TargetHelpPage(self.driver)
        self.target_sign_in = TargetSignIn(self.driver)
