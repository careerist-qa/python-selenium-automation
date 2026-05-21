from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

     class Header(Page):

 SEARCH_FIELD = (By.ID, 'search')
 SEARCH_BTN = (By.XPATH, "//button[@datatest='@web/Search/SearchButton']")

     def search_product(self, search_query: str):
      self.input_text(search_query, *self.SEARCH_FIELD)
      self.click(*self.SEARCH_BTN)
      sleep(10)

# def click_cart(self):
# pass