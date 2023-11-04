from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'