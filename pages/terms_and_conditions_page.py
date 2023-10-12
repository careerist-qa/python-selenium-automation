from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class TermsAndConditionsPage(Page):
    TERMS_AND_CONDITIONS = '/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
    PRIVACY_LINK =

    def open_amazon_tc_page(self,*TERMS_AND_CONDITIONS):
        self.driver.get(f'https://www.amazon.com/dp/{TERMS_AND_CONDITIONS}/')
        sleep(2)
        self.driver.refresh()

    def store_original_window(self):
        return self.get_current_window()

    def click_privacy_link(self):
        self.click(*PRIVACY_LINK)
