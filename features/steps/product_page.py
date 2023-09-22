from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')

@then('Add product to cart')
def add_product_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()

@when("Store Product Name")
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')

