from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


######################################## Given ########################################

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


######################################## When ########################################

@when('Clicking on empty cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']").click()


@when('Clicking on Sign in')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()


######################################## Then ########################################

@then('Verify "Your cart is empty" text shown')
def empty_cart(context):
    expected_text = "Your cart is empty"
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text == actual_text, f'Expected text, "{expected_text}" does not match the actual text," {actual_text}".'


@then('Verify Sign in form opens')
def sign_in_form(context):
    expected_result= "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign in']").text
    assert expected_result == actual_result, f'Expected result, "{expected_result}" does not match the actual result," {actual_result}".'



