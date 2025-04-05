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
# driver.implicitly_wait(4)  # checks for element every 100 ms
driver.maximize_window()
driver.wait = WebDriverWait(driver, timeout=10)

# open the url
driver.get('https://www.google.com/')
# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

# wait for 4 sec

# sleep(4)
# click search button
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable').click()

sleep(5)

# verify search results
assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')
driver.quit()