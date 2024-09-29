from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_TXT = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_into_target_account(self):
        expected_text = 'Sign into your Target account'
        actual_text= self.driver.find_element(*self.SIGN_IN_TXT).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'