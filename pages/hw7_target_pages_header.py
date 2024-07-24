from selenium.webdriver.common.by import By
from pages.hw7_target_pages_base import Hw7PageBase


class Hw7PageHeader(Hw7PageBase):
    SIGN_IN_LINK = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')

    def click_sign_in_link(self):
        self.click_element(*self.SIGN_IN_LINK)
