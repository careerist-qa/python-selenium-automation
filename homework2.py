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

# open a sign-in page
driver.find_element(By.XPATH, '//span[@id="nav-link-accountList-nav-line-1" and text()="Hello, sign in"]').click()
sleep(5)

# Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')

# Email field
signin_email = driver.find_element(By.ID, 'ap_email')
signin_email.clear()
signin_email.send_keys('homework2@qaautomation.com')

# Continue button
driver.find_element(By.XPATH,'//input[@aria-labelledby="continue-announce"]')

# Conditions of use link
driver.find_element(By.XPATH, '//div[@id="legalTextRow"]//a[contains(text(), "Conditions of Use")]')

# Privacy Notice link
driver.find_element(By.XPATH, '//div[@id="legalTextRow"]//a[contains(text(), "Privacy Notice")]')

# Need help link
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]')

# Forgot your password link - not in my browser
# Other issues with Sign-In link - not in my browser

# Shoe on Amazon Business
driver.find_element(By.XPATH, '//*[contains(text(), "Shop on Amazon Business")]')

# Create your Amazon account button
driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')

print("PASS 1. Practice Test Cases")
sleep(10)

# 2. Create a test case for the SignIn page using python & selenium script.
# open the url
driver.get('https://www.target.com/')

# Click SignIn button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(5)

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(5)

# Verify SignIn page opened
driver.find_element(By.ID, 'login')
driver.find_element(By.XPATH, "//button[@id='login']")

print("PASS 2. Homework 2 Test Cases")

sleep(10)

# 3. Optional - test case for search
# open the url
driver.get('https://www.target.com/')

# input a keyword in the search and click
driver.find_element(By.ID, 'search').clear()
driver.find_element(By.ID, 'search').send_keys('shoes')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)
# driver.find_element(By.ID, 'search').send_keys('shoes', Keys.RETURN)

# refresh the page because not load the result page. It seems outside US.
# sleep(5)
# driver.refresh()
# sleep(5)

# verify the result
expected_text = 'shoes'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']//span[contains(text(), 'shoes')]").text
print(actual_text)
assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
print("PASS 3. Optional Test Cases")

driver.quit()