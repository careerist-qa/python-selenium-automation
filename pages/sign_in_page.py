from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_sign_in(self):
        expected_result = 'Sign in'
        actual_result = self.find_element(*self.SIGN_IN).text
        assert expected_result == actual_result, \
            f'Error expected {expected_result} did not match actual {actual_result}'
