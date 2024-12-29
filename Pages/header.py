from selenium.webdriver import Keys

from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class HeaderPage(BasePage):
    SEARCH_BAR=By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']"
    SEARCH_BTN=By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"

    def search_bar(self,product,*locator):
        self.input_text(product,*self.SEARCH_BAR).send_keys(product)
        self.click(*self.SEARCH_BTN)
        sleep(10)
