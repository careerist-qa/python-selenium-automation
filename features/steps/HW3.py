from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then

driver_path = ChromeDriverManager().install()

# init driver
driver = webdriver.Chrome()


@given("Open Target page")
def target_page(context):
    context.driver.get('https://www.target.com/')
    context.driver.get('https://www.target.com/')
    sleep(1)

@when("Click on cart icon")
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='cart 0 items']").click()
    sleep(4)

@then("Verify cart page is present")
def verify_sign(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0").is_displayed()
    print('TEST 1 PASSED')

@when("Click on sign in icon")
def sign_out(context):
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-expanded='false'][aria-label='Account, sign in']").click()
    sleep(1)

@when("Click on sign in button")
def sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(4)

@then("Verify sign in page is present")
def verify_sign(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0").is_displayed()
    print('TEST 2 PASSED')
