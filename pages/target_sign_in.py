from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class TargetSignIn(Page):
    user = (By.ID, 'username')
    pas = (By.ID, 'password')
    login = (By.ID, 'login')
    error = (By.CSS_SELECTOR, 'div.styles__AlertDisplayStyles-sc-vw2fsn-0')

    def enter_user(self, username):
        self.driver.find_element(*self.user).send_keys('gieks@bdfjie.com')


    def enter_pass(self, password):
        self.driver.find_element(*self.pas).send_keys('https://www.target.com/login?client_id')


    def click_sign_in(self):
        self.driver.find_element(*self.login).click()


    def verify_error(self):
        self.driver.find_element(*self.error).is_displayed()

