from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class TermsAndConditionsPage(Page):
    TERMS_AND_CONDITIONS = '/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
    PRIVACY_LINK = 'gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'

    def open_amazon_tc_page(self):
        self.driver.get(f'https://www.amazon.com//gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
        sleep(2)
        self.driver.refresh()

    def store_original_window(self):
        return self.get_current_window()

    def click_privacy_link(self):
        self.click(*self,PRIVACY_LINK)

