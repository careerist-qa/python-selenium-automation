from pages.base_page import BasePage
from pages.Main_page import MainPage
from pages.circle_page import CirclePage
from pages.cart_page import CartPage

from locators import driver


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page=BasePage(driver)
        self.main_page=MainPage(driver)
        self.circle_page=CirclePage(driver)
        self.cart_page=CartPage(driver)

app=Application(driver)
app.base_page.function
app.main_page.function
app.circle_page.function
app.cart_page.function




