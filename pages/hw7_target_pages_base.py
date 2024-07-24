from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Hw7PageBase:
    EMAIL = 'ilvys@putameda.com'
    PASSWORD = '*******'

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_until_visible(self, *locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator),
                               message=f'Element by locator {locator} is not visible'
                               )

    def wait_until_invisible(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element_located(locator),
                               message=f'Element by locator {locator} is still invisible'
                               )
        return True

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def refresh_page(self):
        sleep(1)
        self.driver.refresh()

    def return_text_from_element(self, *locator):
        return self.driver.find_element(*locator).text

    def wait_until_clickable_click(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()
