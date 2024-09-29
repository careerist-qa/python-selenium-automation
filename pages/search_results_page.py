from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.PRODUCT_NAME = None

    def get_product_name(self):
        return self.PRODUCT_NAME

    def verify_results(self, product):
        actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert product in actual_result, f'Expected {product}, got actual {actual_result}'

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def store_product_name(self):
         self.PRODUCT_NAME = self.driver.find_element(*self.CART_ITEM_TITLE).text

    def side_nav_click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN_SIDE_NAV)


