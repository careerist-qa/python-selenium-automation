from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from time import time


class HW8PageBase:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_and_click(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_until_title_contains(self, *title):
        self.driver.wait.until(EC.title_contains(*title))

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_current_window(self):
        window = self.driver.current_window_handle
        print('Current window is %s' % window)
        return window

    def switch_to_window(self):
        original_window = self.driver.current_window_handle
        current_url = self.driver.current_url
        self.driver.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        print(f'All windows are {windows}')
        print(f'Current Url: {current_url}')

        # For Safari
        for window_handle in windows:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        # self.driver.switch_to.window(windows[1])
        print(f'Switched to window {windows[1]}')
        print(f'Current window is {self.driver.current_window_handle}')

    def verify_partial_url(self, partial_url):
        # For Firefox
        self.driver.wait.until(lambda driver: partial_url in driver.current_url)
        current_url = self.driver.current_url
        print(f'Current terms url is {current_url}')
        print(f'Current terms window is {self.driver.current_window_handle}')
        assert partial_url in current_url, f'Expected {partial_url} but got {current_url}'

    def close_window(self):
        self.driver.close()

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print(f'Switched to window {window_id}')

    @staticmethod
    def pause_sleep(s):
        sleep(int(s))

