from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Clicks on orders button")
def click_orders_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()


@then("User can see sign-in page")
def sign_in_verification(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("Verification Complete")


