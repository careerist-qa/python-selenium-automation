from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to'
           '=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%'
           '252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_Account'
           'Flyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2'
           'Fspecs.openid.net%2Fauth%2F2.0')

# Amazon Logo
driver.find_element(By.XPATH, '//a[@class="a-link-nav-icon"]')

# Continue Button
driver.find_element(By.XPATH, '//input[@id="continue"]')

# Need Help Button
driver.find_element(By.XPATH, '//span[class="a-expander-prompt"]')

# Forgot Your Password
driver.find_element(By.XPATH, '//a[@id="auth-fpp-link-bottom"]')

# Other Issues With Sign-In
driver.find_element(By.XPATH, '//a[@id="ap-other-signin-issues-link"]')

# Condition Of Use
driver.find_element(By.LINK_TEXT, "Conditions Of Use")

# Privacy Notice
driver.find_element(By.LINK_TEXT, "Privacy Notice")

driver.close()
