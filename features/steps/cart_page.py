from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_txt(context):
    context.app.cart_page.verify_cart_empty_txt()
