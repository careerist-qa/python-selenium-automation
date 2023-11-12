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

sign_in_page = driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
logo = driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')
email_field = driver.find_element(By.ID, "ap_email")
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
conditions_of_use_link = driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
privacy_notice_link = driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

need_help_link.click()
forgot_your_password_link = driver.find_element(By.ID, "auth-fpp-link-bottom")
other_issues_with_sign_in_link = driver.find_element(By.ID, "ap-other-signin-issues-link")

create_your_amazon_account_button = driver.find_element(By.ID, "createAccountSubmit")


driver.get("https://www.amazon.com/")
driver.find_element(By.ID, "nav-orders").click()

sign_in_header = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
email_input_field = driver.find_element(By.ID, "ap_email")

assert sign_in_header.is_displayed(), 'Error. Sign In header is not visible'
print('Test case passed')

assert email_input_field.is_displayed(), 'Error. Email input field is not present'
print('Test case passed')