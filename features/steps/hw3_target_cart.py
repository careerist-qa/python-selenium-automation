from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target_com(context):
    context.driver.get('https://www.target.com')


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label*='0 items'][data-test='@web/CartLink']").click()
    sleep(2)


@then('Verify "Your cart is empty" message is shown')
def verify_cart_is_empty(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
