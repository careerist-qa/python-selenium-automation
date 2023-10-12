from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.sign_in_page import SignInPage
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.bestsellers_page import BestsellersPage
from pages.product_page import ProductPage
from pages.not_found_page import NotFoundPage
from pages.blog import Blog
from pages.terms_and_conditions_page import TermsAndConditionsPage



class Application:
    def __init__(self,driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.bestsellers_page = BestsellersPage(driver)
        self.product_page = ProductPage(driver)
        self.not_found_page = NotFoundPage(driver)
        self.blog = Blog(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)

