from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart Icon')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "image[href='https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart']").click()
    sleep(6)


@then('Verify "Your cart is empty"')
def verify_cart_empty(context):
    expected = 'Your cart is empty'
    actual = context.driver.find_element(By.CSS_SELECTOR, ".lfA-Dem").text
    assert expected == actual, f'Expected {expected} is not equal to {actual}'
    context.driver.quit()
