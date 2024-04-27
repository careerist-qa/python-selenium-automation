from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    FAVORITES_BTN = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        fav_btn = self.find_element(*self.FAVORITES_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(fav_btn)
        actions.perform()

    def verify_fav_tooltip(self):
        self.verify_text('Click to sign in and save', *self.FAVORITES_TOOLTIP_TXT)

    def verify_search_results(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
