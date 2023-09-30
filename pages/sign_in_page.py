from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_sign_in(self):
       self.verify_text('Sign in', *self.SIGN_IN)

    def verify_partial_url(self,expected_part_of_url):
        self.verify_partial_text(expected_part_of_url)