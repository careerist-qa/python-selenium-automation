from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class TermsConditionsPage(Page):

    PRIVACY_NOTICE = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")

    def open_tc_page(self):
        self.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
        self.driver.refresh()

    def click_on_privacy_notice(self):
        self.driver.find_element(*self.PRIVACY_NOTICE).click()
       # self.wait.until(EC.new_window_is_opened(current_handles))

    def verify_privacy_notice(self):
        self.driver.find_element(By.CSS_SELECTOR, "#helpsearch")

    def store_original_windows(self):
        return self.get_current_window()

