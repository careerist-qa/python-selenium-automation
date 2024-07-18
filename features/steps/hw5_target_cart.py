from time import sleep
from behave import when, then
from selenium.webdriver.common.by import By
import time

CART_SUMMARY = (By.XPATH, '//div[./span[contains(text(), "subtotal")]]')
CART_ITEM_TITLE = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')
    # sleep(2)    # To avoid NoSuchElementException at cart_summary in Verify cart has {amount} items(s)


@then('Verify cart has {amount} itme(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify cart has correct product')
def verify_cart_items(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Product Name: {context.product_name}')
    print(f'Actual Name: {actual_name}')
    assert context.product_name[:20] == actual_name[:20], f"Expected {context.product_name} but got {actual_name}"
    context.tok = time.time()
    elapsed_time = context.tok - context.tic
    print(f'Elapsed time: {elapsed_time:.2f} seconds')
