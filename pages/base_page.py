from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            f'Element not visible by {locator}'
        )

    def wait_until_disappears(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            f'Element still visible by {locator}'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text , f'Expected {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'Url does not contain {expected_partial_url}')

    def verify_url(self, expected_url):
        self.wait.until(EC.url_matches(expected_url), message=f'Url does not contain {expected_url}')

    def save_screenshot(self, name):
        self.driver.save_screenshot(f'{name}.png')
