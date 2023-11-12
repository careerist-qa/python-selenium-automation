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

sign_in_page = driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=RBJHBCPG3QH8ZFVSGPS3&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
logo = driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")
create_account_header = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
name_field = driver.find_element(By.ID, "ap_customer_name")
contact_info_field = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
password_field = driver.find_element(By.ID, "#ap_password")
password_message = driver.find_element(By.CSS_SELECTOR, 'div[class="a-box a-alert-inline a-alert-inline-info auth-inlined-information-message a-spacing-top-mini"]')
password_check_field = driver.find_element(By.CSS_SELECTOR, '[name="passwordCheck"]')
continue_button = driver.find_element(By.CSS_SELECTOR, ".a-button-input")
conditions_of_use = driver.find_element(By.CSS_SELECTOR, 'a[href*="condition_of_use"]')
notification_privacy_notice = driver.find_element(By.CSS_SELECTOR, 'a[href*="notification_privacy_notice"]')
sign_in_for_existing_acc = driver.find_element(By.CSS_SELECTOR, 'a[href*="signin"]')