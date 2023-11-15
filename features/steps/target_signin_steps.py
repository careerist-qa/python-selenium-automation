from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click sign in')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3").click()
    sleep(6)


@when('Click sign in on Navigation Menu')
def click_signin_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify sign in formed open')
def verify_form_open(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']").text
    assert expected == actual, f'Expected {expected} did not match {actual}'
    context.driver.quit()
