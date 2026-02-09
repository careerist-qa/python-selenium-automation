
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@given('Open target.com')
def open_target(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()

# @when('Click on Cart icon')
# def open_cart(context):
#     # context.driver.get('https://www.target.com/cart')
#     context.app.cart_page.open_cart()


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart(context):
    sleep(5)
    context.app.cart_page.verify_empty_cart()





# @then('Verify cart has correct product')
# def verify_product_name(context):
#     # context.product_name => stored before
#     product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
#     print('Name in cart: ', product_name_in_cart)
#     assert context.product_name[:20] == product_name_in_cart[:20], \
#         f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'
#
#
# @then('Verify cart has {amount} item(s)')
# def verify_cart_items(context, amount):
#     cart_summary = context.driver.find_element(*CART_SUMMARY).text
#     assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
