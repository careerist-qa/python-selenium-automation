from behave import when, then
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@then('Verify cart has correct product')
def verify_product_name(context):
    part_name = context.product_name[:30]
    context.app.cart_page.verify_product_name(part_name)
