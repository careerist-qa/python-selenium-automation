from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def open_url(self,url):
        self.driver.get(url)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_until_present(self, locator):
        self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Element {locator} was not present."
        )

    def wait_until_clickable(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} was not present."
        )

    def wait_until_clickable_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} was not present."
        ).click()
