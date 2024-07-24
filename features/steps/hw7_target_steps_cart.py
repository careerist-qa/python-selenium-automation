from behave import given, when, then


@then('HW7 Verify cart has {amount} item(s)')
def verify_amount_items_in_cart(context, amount):
    context.hw7app.hw7_page_cart.verify_cart_item_amount(amount)


@then('HW7 Verify cart has correct product')
def verify_product_in_cart(context):
    context.hw7app.hw7_page_cart.verify_cart_item_tile(context.added_product_title)