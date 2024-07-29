from pages.hw8_target_pages_basic import HW8PageBase
from selenium.webdriver.common.by import By


class HW8PageTC(HW8PageBase):
    def verify_partial_url_tc(self):
        self.verify_partial_url('/terms-conditions')

    def close_tc_window(self):
        self.close_window()

    def switch_to_signin_page_by_id(self, window_id):
        self.switch_to_window_by_id(window_id)
