from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# create a new Chrome browser instance
service = Service(executable_path='/Users/svetlanalevinsohn/careerist/15-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# define once
# will be applied to all find_element
# check for element ever 100 ms
# does not modify the exception
driver.implicitly_wait(5)

driver.wait = WebDriverWait(driver, 3)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('car')

search_btn = (By.NAME, 'btnK')

# Have to be defined in the code where this wait is used
# It checks for the condition to be met every 500 ms
# always fail with TimeoutException
# supports custom conditions, usually taken EC
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search btn not clickable').click()

# verify search results
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
