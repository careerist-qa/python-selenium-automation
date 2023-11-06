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

driver.get('https://www.amazon.com')
driver.find_element(By.ID, 'nav-link-accountList').click()
driver.find_element(By.ID, 'ap_email').click()

actual_result = 'Email'
expected_result = driver.find_element(By.XPATH,"//label[@class='a-form-label']").text


expected_result == actual_result, 'Error, expected text did not match actual result'
print('Test Pass')

driver.quit()

# Amazon logo
driver.find_element(By.XPATH, "//a[@ari-label = 'Amazon']")
# Email field
driver.find_element(By.ID, 'ap_email')
# Continue button
driver.find_element(By.ID, 'continue')
# Conditions of use link
driver.find_element(By.XPATH, "//a[text() = 'Condition of use']")
# Privacy Notice link
driver.find_element(By.XPATH, "//a[text() = 'Privacy Notice']")
# Need help link
driver.find_element(By.XPATH, 'auth-fpp-link-bottom')
# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')
# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
