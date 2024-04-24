class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def find_elements(self, *locator):
        self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)