from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    def open_main_page(self):
        context.app.main_page.open_main_page()

        context.driver.find_element(By.ID, 'search').send_keys(product)
        context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()



