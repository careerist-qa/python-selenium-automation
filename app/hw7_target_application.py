from pages.hw7_target_pages_base import Hw7PageBase
from pages.hw7_target_pages_header import Hw7PageHeader
from pages.hw7_target_pages_main import Hw7PageMain
from pages.hw7_target_pages_login import Hw7PageLogin
from pages.hw7_target_pages_search import Hw7PageSearch
from pages.hw7_target_pages_product import Hw7PageProduct
from pages.hw7_target_pages_cart import Hw7PageCart


class Hw7Application:
    def __init__(self, driver):
        self.driver = driver
        self.hw7_page_base = Hw7PageBase(self.driver)
        self.hw7_page_main = Hw7PageMain(self.driver)
        self.hw7_page_header = Hw7PageHeader(self.driver)
        self.hw7_page_login = Hw7PageLogin(self.driver)
        self.hw7_page_search = Hw7PageSearch(self.driver)
        self.hw7_page_product = Hw7PageProduct(self.driver)
        self.hw7_page_cart = Hw7PageCart(self.driver)
