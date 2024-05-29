from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class TargetHelpPage(Page):
    dropdown = (By.CSS_SELECTOR, '[onchange="changeItem()"]')
    dif_page = (By.ID, 'ui-id-1')

    def open_help_page(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle')

    def dropdown_present(self):
        drop = self.find_element(*self.dropdown)
        select = Select(drop)
        select.select_by_value('Orders & Purchases')


    def dropdown_select(self):
        self.driver.find_element(*self.dropdown).click()
        self.driver.find_element(*self.dropdown).click()

    def page_change(self):
        self.driver.find_element(*self.dif_page).is_displayed()

