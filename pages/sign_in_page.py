from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")
    EMAIL_INPUT = (By.ID, 'ap_email')

    def verify_sign_in_open(self):
       self.verify_text('Sign in', *self.SIGN_IN)
       self.driver.find_element(*self.EMAIL_INPUT)

    def verify_partial_url(self, expected_part_of_url):
        self.verify_partial_text(expected_part_of_url)
