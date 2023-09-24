from pages.base_page import Page
from selenium.webdriver.common.by import By
class MainPage(Page):

    def open_main(self):
        self.driver.get('https://www.amazon.com/')

    def click_returns_orders(self):
        self.driver.find_element(By.ID, "nav-orders").click()