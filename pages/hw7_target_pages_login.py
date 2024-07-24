from pages.hw7_target_pages_base import Hw7PageBase
from selenium.webdriver.common.by import By


class Hw7PageLogin(Hw7PageBase):
    SIGN_IN_FORM = (By.CSS_SELECTOR, 'form[method="post"]')
    SIGN_IN_USERNAME = (By.ID, 'username')
    SIGN_IN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')

    def verify_login_form(self):
        self.wait_until_visible(*self.SIGN_IN_FORM)

    def input_email_and_password(self):
        self.input_text(self.EMAIL, *self.SIGN_IN_USERNAME)
        self.input_text(self.PASSWORD, *self.SIGN_IN_PASSWORD)

    def click_on_sign_in_button(self):
        self.click_element(*self.LOGIN_BUTTON)
        # self.wait_until_invisible(*self.SIGN_IN_FORM)




