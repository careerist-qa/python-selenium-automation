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

#Amazon
driver.find_element(By.CSS_SELECTOR,'a-section.a-spacing-medium.a-text-center')
#Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
#Your name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
#Mobile number or email
driver.find_element(By.CSS_SELECTOR, '#ap_email')
#Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')
#Re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
#Create your Amazon account(Continue)
driver.find_element(By.CSS_SELECTOR, '#continue')
#Conditions of Use
driver.find_element(By.CSS_SELECTOR,"#legalTextRow a[href*='Conditions of Use']")
#Privacy Notice
driver.find_element(By.CSS_SELECTOR,"#legalTextRow a[href*='Privacy Notice']")
#Sign-in
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')




