from pages.main_page import MainPage
from pages.header import Header
from pages.not_found_page import NotFoundPage
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.cart_page import CartPage
from pages.blog import Blog
from pages.privacy_notice_page import PrivacyNoticePage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.not_found_page = NotFoundPage(driver)
        self.header = Header(driver)
        self.blog = Blog(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.cart_page = CartPage(driver)
        self.privacy_notice_page = PrivacyNoticePage(driver)



