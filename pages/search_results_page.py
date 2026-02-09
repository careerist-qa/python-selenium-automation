from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):
    search_word = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    ADD_TO_CART_SECOND = (By.CSS_SELECTOR, '[data-test="@web/AddToCart/Fulfillment/ShippingSection"] button[id*="addToCartButton"]')

    def verify_search_result(self):
        actual_text = self.find_element(*self.search_word).text  #from pro_sear.py
        assert 'tea' in actual_text, f'Expected text "tea" not in actual text {actual_text}'

    def click_add_to_cart(self):
        sleep(20)
        self.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
        self.wait_until_clickable_click(self.ADD_TO_CART_SECOND)
