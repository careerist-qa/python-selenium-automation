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

driver.get('https://www.amazon.com/ap/register?openid.return_to=https%3A%2F%2Ftrack.amazon.com%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_shippingrecipientcentral_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon") #Amazon logo
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small") #'Create Account' Text
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name") #Your Name field
driver.find_element(By.CSS_SELECTOR, "#ap_email") #Email field
driver.find_element(By.CSS_SELECTOR, "#ap_password") #Password field
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content") #Password length
driver.find_element(By.CSS_SELECTOR, "#ap_password_check") #Re-enter Password
driver.find_element(By.CSS_SELECTOR, "#continue") #Create account button
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']") #Conditions of Use
driver.find_element(By.CSS_SELECTOR,"[href*='notification_privacy_notice']") #Privacy Notice
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis") #Exsisting account Sign in