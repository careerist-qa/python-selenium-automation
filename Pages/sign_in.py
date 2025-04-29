from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignPage(BasePage):
    Terms_conditions = (By.XPATH,"//a[contains(text(),'Terms')]")
    EMAIL = (By.CSS_SELECTOR, "#username")
    CONTINUE = (By.CSS_SELECTOR, "#login" )
    PASSWORD = (By.CSS_SELECTOR, "#password")
    SIGN_IN = (By.CSS_SELECTOR, "#login")
    ERROR = (By.CSS_SELECTOR, "#password--ErrorMessage")


    def open_sign_in(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_request_username')

    def enter_email(self):
        self.input_text("katie@gmail.com ",*self.EMAIL)

    def click_continue(self):
        self.click(*self.CONTINUE)

    def enter_password(self):
        self.input_text("password",*self.PASSWORD)

    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def click_terms(self):
        self.click(self.Terms_conditions)

    def verify_terms_opened(self):
        self.verify_partial_url('terms-conditions')

    def verify_error_message(self):
        self.verify_text("Please enter a valid password",*self.ERROR)





