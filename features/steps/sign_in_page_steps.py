from behave import given, when, then
from selenium.webdriver.common.by import By

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL_INPUT = (By.ID, 'ap_email')


@then('Verify sign in page opened')
def verify_signin_opened(context):
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    assert actual_text == 'Sign in', f'Expected Sign in but got {actual_text}'
    # Verify email field present
    context.driver.find_element(*EMAIL_INPUT)
