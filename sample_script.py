from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# Implicit
# driver.implicitly_wait(5)  # up to 5 sec / applied to find_element, checks for element ever 100ms

# Explicit
driver.wait = WebDriverWait(driver, timeout=10)  # up to 10 sec / checks for element ever 500ms

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

search_btn = (By.NAME, 'btnK')
# Make sure not to use * for locators when working with EC:
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search btn not clickable').click()

# click search button
# driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()