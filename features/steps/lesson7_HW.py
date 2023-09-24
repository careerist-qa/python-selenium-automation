from behave import given, when, then



@when('Click on cart icon')
def click_on_cart(context):
    context.app.header.click_on_cart()

@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()