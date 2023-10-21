from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
# populate search:
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('mug')
# click on search icon:
driver.find_element(By.ID, 'nav-search-submit-button').click()

# Verification:
expected_result = '"mug"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_result == actual_result, f'Error. Expected text {expected_result} did not match actual {actual_result}'
print('Test case passed!')

driver.quit()
