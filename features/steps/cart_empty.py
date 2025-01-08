from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Target main page")
def target_main_page(context):
    context.app.Main_page.open_target()


@when("Click on Cart icon")
def click_cart_icon(context):
    context.app.header.click_cart_icon().click()

@then("Verify “Your cart is empty” message is shown")
def verify_cart_empty(context):
    expected_text = "Your cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"div[data-test='boxEmptyMsg']").text
    assert expected_text in actual_result,f'{expected_text} not in {actual_result}'
    context.app.cart_empty.verify_cart_empty(actual_result)
