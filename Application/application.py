from Pages.base_page import BasePage
from Pages.Main_page import MainPage
from Pages.header import HeaderPage
from Pages.cart_messages import Cart
from Pages.search_results_page import SearchResultsPage
from Pages.chips_page import ChipsPage
from Pages.sign_in import SignPage
from Pages.terms_conditions_page import TermsConditionsPage
from Pages.target_help_page import TargetHelpPage




class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page=BasePage(driver)
        self.Main_page=MainPage(driver)
        self.header_page=HeaderPage(driver)
        self.search_results_page=SearchResultsPage(driver)
        self.cart_messages=Cart(driver)
        self.chips_page = ChipsPage(driver)
        self.sign_in=SignPage(driver)
        self.terms_conditions_page=TermsConditionsPage(driver)
        self.target_help_page=TargetHelpPage(driver)










