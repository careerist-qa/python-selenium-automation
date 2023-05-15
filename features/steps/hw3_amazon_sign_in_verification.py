from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, "ap_email")
ORDERS_BTN = (By.XPATH, "//a[@id='nav-orders']")


@when("Clicks on orders button")
def click_orders_button(context):
    context.driver.find_element(*ORDERS_BTN).click()


@then("User can see sign-in page")
def sign_in_verification(context):
    actual_text = context.driver.find_element(*SIGNIN_HEADER).txt
    assert actual_text == "Sign in", f"Expected Sign in header but got {actual_text}"
    context.driver.find_element(*EMAIL).send_keys("Verification Complete")


