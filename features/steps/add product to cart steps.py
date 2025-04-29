from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("Click on Grocery")
def click_grocery(context):
    context.app.header.click_grocery()


@when("Click on Snacks")
def click_snacks(context):
    context.app.header.click_snacks()


@when("Click on Chips")
def click_chips(context):
    context.app.header.click_chips()


@when("Click on Add to cart for Doritos")
def click_add_to_cart(context):
    context.app.chips_page.click_add_to_cart()


@when("Click on Add to cart side nav")
def click_add_to_cart_side_nav(context):
    context.app.header.click_add_to_side()


@then("Verify if {product} is shown")
def verify_product(context,product):
    context.app.cart_messages.product_in_cart(product)


