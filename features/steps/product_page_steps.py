from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'li[id*=color_name]')
CURRENT_COLOR = (By.CSS_SELECTOR, '.selection')

@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.app.product_page.open_product(product_id)

@then('Add product to cart')
def add_product_to_cart(context):
    context.app.product_page.product_add_to_cart()



@when("Store Product Name")
def get_product_name(context):
    PRODUCT_NAME_VALUE = context.app.cart_page.product_name_get()
    print(context.app.cart_page.product_name_get())

@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Beige', 'Black', 'Dark Brown']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    print(colors)
    print(len(colors))

    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        print(current_color)
        actual_colors.append(current_color)

    print(actual_colors)

    assert actual_colors == expected_colors
