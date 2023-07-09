from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    ORDERS_BTN = (By.ID, 'nav-orders')
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)
