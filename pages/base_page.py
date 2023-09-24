class Page:

    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text):
        e = self.driver.find_element(*locator)
        e.send_keys(text)