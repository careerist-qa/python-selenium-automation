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
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=77J0CGYVZ1HQVZVB3Z4R&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(15)
# locate element:
# driver.find_element() By. / value
#By CSS, by class
driver.find_element(By.CSS_SELECTOR,".a-icon-logo")
# By CSS, by class
driver.find_element(By.CSS_SELECTOR,".a-spacing-small")
# By CSS, by ID
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")
# By CSS, by ID
driver.find_element(By.CSS_SELECTOR,"#ap_email")
# By CSS, by ID
driver.find_element(By.CSS_SELECTOR,"#ap_password")
# By CSS, by ID
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
# By CSS, by ID
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
# By CSS, by ID
driver.find_element(By.CSS_SELECTOR,"#continue")
# By CSS, from parent => to child, separate by space:
driver.find_element(By.CSS_SELECTOR, ".a-box-inner #legalTextRow [href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")
#By CSS, by class
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")
