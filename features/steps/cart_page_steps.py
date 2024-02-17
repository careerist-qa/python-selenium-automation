from selenium.webdriver.common.by import By
from behave import given, when, then

CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has correct multiple products')
def verify_product_names(context):
    # Grab title text of every product in the cart and store in actual_names:
    actual_names = [product.text for product in context.driver.find_elements(*CART_ITEM_TITLE)]
    # Sort lists before verification:
    context.product_names.sort()
    actual_names.sort()
    assert context.product_names == actual_names, f'Expected {context.product_names} did not match {actual_names}'


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()
