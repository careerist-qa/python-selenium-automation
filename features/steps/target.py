from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(3)


@then('Verify cart Empty message shown')
def verify_cart_empty(context):
    expected_text='Your cart is empty'
    actual_text= context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(3)


@when('From right side navigation menu, click Sign in')
def click_right_side_nav_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


@then('Verify Sign into your Target account text is shown')
def verify_sign_into_target_account(context):
    expected_text = 'Sign into your Target account'
    sleep(5)
    actual_text= context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    print(actual_text)
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'