from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CirclePage(Page):
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")

    def open_circle(self):
        self.open_url('https://www.target.com/circle')

    def verify_can_click_tabs(self):
        self.wait_for_element_appear(*self.BONUS_TAB)  # Wait for Bonus tab to fully load
        tabs = self.find_elements(*self.TABS)

        current_url = ''
        for i in range(len(tabs)):  # [0, 1, 2, 3]
            self.find_elements(*self.TABS)[i].click()
            # sleep(2)

            self.wait_for_url_to_change(current_url)
            current_url = self.driver.current_url
