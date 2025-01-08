from selenium.webdriver.common.by import By
from behave import given, when, then


@when('user clicks on sign in button')
def sign_in(context):
    context.app.header.sign_in.click()

@when('user clicks on side navigation side in button')
def side_navigation(context):
    context.app.header.side_navigation.click()

@then('Verify if Sign in message is displayed')
def verify_sign_in(context):
    expected_message = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"//span[text()='Sign into your Target account']")
    assert expected_message == actual_result, f'{expected_message} != {actual_result}'
    context.app.header.verify_sign_in()