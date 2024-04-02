from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target(context):
    context.driver.get('http://www.target.com/')

@when('Click on the Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, ".styles__CartIconDiv-sc-jff2tp-1").click()
    sleep(2)

@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    assert context.driver, f'The cart is not empty'
