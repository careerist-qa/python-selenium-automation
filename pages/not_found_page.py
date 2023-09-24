from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class NotFoundPage(Page):
    Dog_IMG = (By.CSS_SELECTOR, 'img#d')



    def click_dog_img(self):
        self.click(*self.Dog_IMG)
