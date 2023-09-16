from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@then('Verify Sign-in page is opened')
def verify_sign_in(context):
    expected_result = 'Sign In'
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]")
    assert expected_result == actual_result, f'Error expected {expected_result} did not match actual {actual_result}'
