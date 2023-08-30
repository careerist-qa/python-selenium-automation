from selenium.webdriver.common.by import By
from behave import *
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
OPEN_CART_PAGE = (By.CSS_SELECTOR, "#nav-cart-text-container")
VERIFY_CART_AMOUNT = (By.CSS_SELECTOR, '.a-dropdown-prompt')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
    sleep(2)
    context.driver.refresh()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(1)


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*OPEN_CART_PAGE).click()
    sleep(1)


@then('Verify cart has item(s)')
def verify_cart_amount(context):
    context.verify_cart_amount = context.driver.find_element(*VERIFY_CART_AMOUNT).text
    print(f'Current product: {context.verify_cart_amount}')


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:10] in actual_name, f'Expected {context.product_name} but got {actual_name}'


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Apricot', 'Azure Blue', 'B-apricot'] # 0, 1, 2, 3
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

        assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'



