from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class TermsConditionsPage(BasePage):

    def verify_terms(self):
            self.verify_partial_text('terms-conditions')


