from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# init driver
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

# Verify Sign in header
expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

# Verify email field present
driver.find_element(By.ID, 'ap_email')

# Verify Legal text
expected_text = "Conditions of Use and Privacy Notice."
actual_text = driver.find_element(By.ID, 'legalTextRow').text
assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

driver.quit()
