from selenium.webdriver.common.by import By
from pages.hw7_target_pages_base import Hw7PageBase


class Hw7PageMain(Hw7PageBase):
    URL_TARGET = 'https://www.target.com/'
    NAV_SIGN_IN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    SEARCH_INPUT= (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    SIGN_IN_FORM = (By.CSS_SELECTOR, 'form[method="post"]')

    def open_target_home_page(self):
        self.open_url(self.URL_TARGET)

    def click_nav_sign_in_list(self):
        self.wait_until_visible(*self.NAV_SIGN_IN)
        self.click_element(*self.NAV_SIGN_IN)

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click_element(*self.SEARCH_BUTTON)

    def verify_sign_in_form_disappear(self):
        assert self.wait_until_invisible(*self.SIGN_IN_FORM), f'Expected {self.SIGN_IN_FORM} is disappeared but still exist'

    def verify_sign_in_url_disappear(self):
        current_url = self.get_current_url()
        assert 'signin' not in current_url, f'Expected "signin" is not in current URL.'



