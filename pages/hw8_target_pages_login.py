from pages.hw8_target_pages_basic import HW8PageBase
from selenium.webdriver.common.by import By


class HW8PageLogin(HW8PageBase):
    URL_TARGET = 'https://www.target.com/'
    TITLE_LOGIN = 'Login'
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    SIGN_IN_BUTTON_NAV = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    TC_LABEL = (By.CSS_SELECTOR, '[aria-label*="terms"]')

    def open_target_sign_login_page(self):
        self.open_url(self.URL_TARGET)
        self.wait_and_click(*self.SIGN_IN_BUTTON)
        self.wait_and_click(*self.SIGN_IN_BUTTON_NAV)

    def store_original_sign_in_page(self):
        return self.get_current_window()

    def click_tc_link(self):
        self.wait_until_title_contains(self.TITLE_LOGIN)
        self.find_element(*self.TC_LABEL).click()

    def switch_to_tc_window(self):
        self.switch_to_window()

    def verify_partial_url_signin(self, partial_url):
        self.verify_partial_url(partial_url)

