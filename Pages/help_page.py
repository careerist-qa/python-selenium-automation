from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


# #class HelpPage(BasePage):
#     TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
#     HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
#
#     def _get_header_locator(self, header):
#         # HEADER (By.XPATH, "//h1[text()=' {SUBSTRING}']") => (By.XPATH, "//h1[text()=' Returns']")
#         return [self.HEADER[0], self.HEADER[1].replace('{SUBSTRING}', header)]
#
#
#     def open_help_page(self):
#         self.open_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")
#
#
#     def choose_topic(self):
#         self.select_topic(*self.TOPIC_SELECTION_DD)
#
#
#     def verify_target_help_page_opened(self):
#         self.verify_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")
#
#
#     def verify_topic_page_opened(self,header):
#         locator = self._get_header_locator(header)
#         print(locator)
#         self.wait_for_element_visible(locator)







