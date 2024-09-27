from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    HEART_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TOOLTIP = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")

    def hover_favorites(self):
        heart_icon = self.find_element(*self.HEART_ICON)

        actions = ActionChains(self.driver)
        actions.move_to_element(heart_icon)
        actions.perform()

    def verify_favorites(self):
        self.wait_for_element_to_appear(*self.FAV_TOOLTIP)

    def verify_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)

    def verify_results_url(self, product):
        self.verify_partial_url(product)