from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver import Keys


ADD_TO_CART = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
SIDE_NAV_ADD_TO_CART = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(6)
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(2)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART).click()
