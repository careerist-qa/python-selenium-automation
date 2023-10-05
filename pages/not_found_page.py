from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class NotFoundPage(Page):
    DOG_IMG = (By.CSS_SELECTOR, 'img#d')

    def store_original_window(self):
        return self.get_current_window()

    def click_dog_img(self):
        self.click(*self.DOG_IMG)
