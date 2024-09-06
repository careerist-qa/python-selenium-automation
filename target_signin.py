from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open target.com
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1/span").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'

# OR:
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

# Make sure login button is shown
driver.find_element(By.ID, 'login')

