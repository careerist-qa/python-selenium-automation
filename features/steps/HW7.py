from selenium.webdriver.common.by import By
from behave import given, when, then

from time import sleep

orders = (By.ID, "nav-orders")
empty = (By.ID, "div.sc-your-amazon-cart-is-empty")


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.browser.find_element(*orders).click()
    sleep(2)


@then('Verify "Your Shopping Cart is empty." text present')
def verify_amazon_orders_text(context):
    context.app.base_page.verify_partial_text("Your Amazon Cart is empty", *empty)


@when("Click on cart iconA")
def sign_in(context):
    context.driver.find_element(By.ID, "nav-cart").click()
    sleep(4)
