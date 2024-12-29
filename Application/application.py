from Pages.base_page import BasePage
from Pages.Main_page import MainPage
from Pages.header import HeaderPage
from Pages.cart_empty import Cart
from Pages.search_results_page import SearchResultsPage
from locators import driver


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page=BasePage(driver)
        self.main_page=MainPage(driver)
        self.header_page=HeaderPage(driver)
        self.search_results_page=SearchResultsPage(driver)
        self.cart=Cart(driver)

app=Application(driver)
app.base_page.function
app.Main_page.function
app.header.function
app.cart_empty.function
app.search_results_page.function





