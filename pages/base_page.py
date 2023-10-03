from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self,*locator):
        self.driver.find_element(*locator).click()

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def store_value(self,*locator):
        pass

    def get_current_window(self):
        return self.driver.current_window.handle

    def get_original_windows(self):
        return self.driver.window.handles

    def wait_for_element_clickable_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator),message = 'Element not clickable')
        e.click()
    def wait_for_element_clickable(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator),message='Element not clickable')

    def wait_for_element_disappear(self, *locator):
        e = self.wait.until(EC.invisibility_of_element_located(locator) , message='Element did not disappear')

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Error expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error expected partial text {expected_text} was not in actual {actual_text}'

    def verify_partial_url(self,expected_part_of_url):
        self.wait.until(EC.url_contains(expected_part_of_url))
