# Link between environment layer to pages layer
from pages.hw6_base_page import Hw6Page
from pages.hw6_main_page import Hw6MainPage
from pages.hw6_header_page import Hw6HeaderPage
from pages.hw6_search_page import Hw6SearchResultPage
from pages.hw6_cart_page import Hw6CartPage


class Hw6Application:
    #  Construct a Hw6Page instance with webdriver.Chrome passed from environment
    def __init__(self, driver):
        self.driver = driver
        self.hw6_base_page = Hw6Page(self.driver)
        self.hw6_main_page = Hw6MainPage(self.driver)
        self.hw6_header_page = Hw6HeaderPage(self.driver)
        self.hw6_search_page = Hw6SearchResultPage(self.driver)
        self.hw6_cart_page = Hw6CartPage(self.driver)