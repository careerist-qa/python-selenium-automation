from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

PRODUCT_NAME = (By.CSS_SELECTOR, '#sc-active-cart-li')

@when ('Click Cart')
def click_cart(context):
    context.app.cart_page.click_cart()


@then('Verify product is {expected_result}')
def check_product_added(context,expected_result):
    context.app.cart_page.verify_product_added(expected_result)


@then('Verify cart has correct product')
def verify_product_name(context, expected_text):
    context.app.cart_page.verify_product_correct(PRODUCT_NAME)

@then('Verify {string} text is present')
def empty_cart_verify(context, string):
    context.app.cart_page.verify_empty_cart(string)
