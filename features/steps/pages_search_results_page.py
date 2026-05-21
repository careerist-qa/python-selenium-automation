from selenium.webdriver.common.by import By
from pages.base_page import Page

 class SearchResultsPage(Page):
  SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 
'styles_resultCount')]")

   def verify_search_results(self, product: str):
   actual_result =

   self.find_element(*self.SEARCH_RESULT_COUNT_TEXT).text

assert product in actual_result, f'Expected "{product}" not in
actual "{actual_result}"'