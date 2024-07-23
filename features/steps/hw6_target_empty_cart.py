from behave import given, when, then


@then('Verify "Your cart is empty" message is shown by Page')
def verify_cart_is_empty(context):
    context.hw6app.hw6_cart_page.verify_empty_message_contain()
    context.hw6app.hw6_cart_page.verify_empty_message_equal()