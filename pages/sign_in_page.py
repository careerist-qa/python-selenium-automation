from selenium.webdriver.common.by import By

from pages.base_page import Page
from behave import when, then


class SignIn(Page):
    SIGNIN_BTN = (By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
    SIDE_NAV_BTN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    VERIFY_SIGNIN_OPEN = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def click_sign_in(self):
        self.click(*self.SIGNIN_BTN)

    def side_nav_sign_in_btn(self):
        self.wait_until_clickable(*self.SIDE_NAV_BTN)

    def verify_sign_in_shown(self, expected_text,  *locator):
        self.verify_sign_in_shown(*self.VERIFY_SIGNIN_OPEN)
