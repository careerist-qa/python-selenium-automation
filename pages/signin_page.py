from pages.base_page import Page
from pages.main_page import MainPage

class SigninPage(Page):

    def verify_signin_page(self):
        self.driver.find_element(By.ID, "ap_email").click()