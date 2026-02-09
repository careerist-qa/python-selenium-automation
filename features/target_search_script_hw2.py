from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(6)

# verification:
# by finding 1 element
# driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
# print('Test case passed')

# by checking text
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
expected_text = 'tea'

assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
print('Test case passed')

# Note: please do not use if/else for verification, you test case must fail with an Exception if a feature is broken
# sleep(10)