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
#Amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon-logo")
#Create account text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# Your name section
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
#Email section
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
#Password
driver.find_element(By.CSS_SELECTOR, "#ap_password")
#FYI I don't have "Forgot your password link and Other issue with Sign-in link"
#Re-enter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
#Continue button
driver.find_element(By.CSS_SELECTOR, "[type=submit]")
#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*=ap_register_notification_condition_of_use]")
#Policy
driver.find_element(By.CSS_SELECTOR,"a[href*=ap_register_notification_privacy_notice]")
#Sing in
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")
