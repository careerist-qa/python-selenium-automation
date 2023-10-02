from pages.base_page import Page
from selenium.webdriver.common.by import By

class BestsellersPage(Page):
    def verify_bestsellers_page_open(self):
        LINKS = (By.CSS_SELECTOR, "class*='nav-tab-all_style_zg-tabs-li")

        actual_result = self.driver.find.element(LINKS)
        expected_result = len(LINKS) == 5
        assert actual_result == expected_result, f'Error expected {expected_result} does not match {actual_result}'