from selenium.webdriver.common.by import By
from behave import when, then

CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
