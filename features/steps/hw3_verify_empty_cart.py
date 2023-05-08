from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click on cart button")
def click_cart_button(context):
    context.driver.find_element(By.ID, "nav-cart").click()


@then("User can see empty cart message")
def verify_empty_cart(context):
    context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]")



