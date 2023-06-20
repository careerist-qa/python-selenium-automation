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
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# driver.find_element(By.ID,'nav-link-accountList-nav-line-1')
# print('opened sign in')
# newcustomer=driver.find_element(By.CSS_SELECTOR, "a[href*='3Dnav_newcust']")
# print('opened registeration')
# newcustomer.click()
# print('page opened')
# sleep(5)

print('page opened2')
sleep(5)
driver.find_element(By.CSS_SELECTOR,"i.a-icon ")
sleep(2)

driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")
sleep(2)

driver.find_element(By.CSS_SELECTOR,"input#ap_customer_name")
sleep(1)

driver.find_element(By.ID, 'ap_email')
sleep(2)

driver.find_element(By.ID, 'ap_password')
sleep(1)

driver.find_element(By.ID, 'ap_password_check')
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'input#continue')
sleep(2)

driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
sleep(2)

driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
sleep(2)

driver.find_element(By.CSS_SELECTOR, 'a[href*="max_auth_age"]')
sleep(2)

driver.quit()