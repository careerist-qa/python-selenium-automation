from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# 1. Find the most optimal locators for Create Account on amazon.com (Registration) page elements:
#Amazon log
$$("#a-page [href*='frn_logo']")
#Create account
$$("#ap_register_form [href*='ap_register_form']")
#Your name
$$("#ap_customer_name_context_message_section")
#Email
$$("#ap_email")
#Password
$$("#ap_password")
#Passwords must be at least 6 characters
$$("#auth-password-requirement-info")
#Re-enter password
$$("#ap_password_check")

#Condition of use
$$("#legalTextRow [href*='condition_of_use']")
#Privacy notice
$$("#legalTextRow [href*='<a privacy_notice']")
#Sing in
$$("#a-row [href*='Sing in']")

#2.Create a test case using BDD that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown:
#Target_search_featuer
 Scenario: 'Your cart is empty' search is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then("Verify 'Your cart is empty' message is shown")
def virify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_results = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text == actual_results, f'Expected {expected_text} did not match actual {actual_results}'
    print("Test passed")


#3. Create a test case using BDD to verify that a logged out user can navigate to Sign In:
 Scenario: 'Sign into your Target account' search is shown for sing in
    Given Open target main page
    When Click on sing in icon
    Then Verify 'Sign into your Target account'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open target.com
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

# Verification
expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'

# OR:
# driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

# Make sure login button is shown
driver.find_element(By.ID, 'login')