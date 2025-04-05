from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# Open Amazon Sign-In page
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")


#Amazon logo
driver.find_element(By.XPATH, "//a[@class='a-logo']")

#Email field
driver.find_element(By.XPATH, "//input[@type='email' or @name='email']")

#Continue button
driver.find_element(By.XPATH, "//input[@id='continue']")

#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'privacy_notice')]")

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.XPATH, "//a[contains(@href, 'forgotpassword')]")

#Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_popup')]")

#Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

#Create a test case for the SignIn page using python & selenium script.
# Open Target
driver.get("https://www.target.com/")

#Click SignIn button
driver.find_element(By.XPATH, "//a[@id='account']")

#Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]")

#Verify SignIn page opened:
driver.find_element(By.XPATH, "//h1[text()='Sign into your Target account']")

#SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.XPATH,"//button[contains(@type,'submit') and contains(text(),'Sign in')]")





