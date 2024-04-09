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
sleep(15)

#click signin
driver.find_element(By.ID, 'nav-link-accountList').click()

#click create account
driver.find_element(By.CSS_SELECTOR, "a#createAccountSubmit").click()
sleep(3)

#amazon lable
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#create account
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

#your name
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

#mobile number or email
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

#password
driver.find_element(By.ID, "ap_password")

#pw must be atleast 6 char
driver.find_element(By.XPATH, "//div[@class='a-alert-content']")

#re-enter pw
driver.find_element(By.ID, "ap_password_check")

#continue link
driver.find_element(By.ID, "continue")

#condition of use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

#privacy notice
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#sign in link
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")