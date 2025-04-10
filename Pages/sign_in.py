from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignPage(BasePage):
    Terms_conditions = (By.XPATH,"//a[contains(text(),'Terms')]")

    def open_sign_in(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_request_username')


    def click_terms(self):
        self.click(self.Terms_conditions)


    def verify_terms_opened(self):
        self.verify_partial_url('terms-conditions')





