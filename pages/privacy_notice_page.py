from pages.base_page import Page
from selenium.webdriver.common.by import By


class PrivacyNoticePage(Page):

    Privacy_Notice = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")

    def store_original_window(self):
        return self.get_current_window()

    def click_on_amazon_privacy_notice_link(self):
        self.click(*self.Privacy_Notice)

    def switch_to_the_newly_opened_window(self):
        return self.switch_to_new_window()

    def verify_amazon_privacy_notice_page_is_open(self):
        self.verify_partial_url('https://www.amazon.com/gp/help/customer/display')

    def user_can_close_new_window_and_switch_back_to_original(self):
        self.close_page()
        return self.driver.get_current_window()


