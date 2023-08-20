class Page:

    def __int__(self, driver):
        self.driver = driver
    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self):
        self.driver.find_element


    def input_text(self):
        pass