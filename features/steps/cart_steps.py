from selenium.webdriver.common.by import By
from behave import given, when, then

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify Cart Empty message shown')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

from behave import given, when, then
from pages.home_page import HomePage
from pages.cart_page import CartPage

@given('Open Target main page')
def step_open_main_page(context):
    context.home_page = HomePage(context.driver)
    context.home_page.load()

@when('Click on cart icon')
def step_click_cart(context):
    context.home_page.click_cart()
    context.cart_page = CartPage(context.driver)

@then('Verify Cart Empty message shown')
def step_verify_cart_empty_message(context):
    assert context.cart_page.is_cart_empty_message_displayed(), "Empty cart message not displayed"