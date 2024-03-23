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
driver.get('https://www.target.com/')

# Enter 'coffee' in search field
driver.find_element(By.ID, 'search').send_keys('coffee')
# Click search btn
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)

# Verification
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert 'coffee' in actual_text, f'Error! Text coffee not in {actual_text}'

driver.quit()