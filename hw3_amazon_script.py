from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to ChromeDriver executables
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 1. Practice with locators
# open the url
# driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
driver.get('https://www.amazon.com/')

# open sign in page
driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
sleep(2)

# open create account page
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
sleep(2)

# verify amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

# verify create account header
# driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small' and contains(text(), 'Create account')]")

# verify customer name input
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name[placeholder='First and last name']")

# verify email input
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

# verify password input
driver.find_element(By.CSS_SELECTOR, "input#ap_password[placeholder*='6 char']")

# verify password check input
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check[aria-required='true']")

# verify continue button
driver.find_element(By.CSS_SELECTOR, "span#auth-continue")

# verify legal condition of use
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='condition_of_use']")

# verify legal privacy notice
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='privacy_notice']")

# verify create business account
driver.find_element(By.CSS_SELECTOR, "#ab-enhanced-registration-link")

# verify sign in link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis[href*='signin']")

print("PASS Create account GUI")

sleep(2)