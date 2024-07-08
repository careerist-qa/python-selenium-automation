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

# #Elements I found by ID:
driver.find_element(By.ID, 'ap_email') # Email field
driver.find_element(By.ID, 'continue') # Continue button
driver.find_element(By.ID, 'auth-fpp-link-bottom') # Forgot your password link
driver.find_element(By.ID, 'ap-other-signin-issues-link') # Other issues with Sign-In link
driver.find_element(By.ID, 'createAccountSubmit') # Create your Amazon account button


#Elements I found by XPATH
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']") # Amazon logo
driver.find_element(By.XPATH, "//a[contains(@href,'condition_of_use')]") # Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'notification_privacy_notice')]") # Privacy Notice link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']") # Need help link
