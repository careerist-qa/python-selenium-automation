from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://www.target.com"
    CART_ICON = (By.ID, "utilityNav-cart")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def click_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
