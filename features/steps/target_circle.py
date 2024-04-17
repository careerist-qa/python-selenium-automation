from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, "div.cell-item-content")


@given('Open target circle page')
def open_target_circle(context):
    context.driver.get("http://target.com/circle")
    sleep(9)


@then('Verify number of benefits')
def verify_number_of_benefits(context):
    elements = context.driver.find_elements(*BENEFIT_CELLS)
    expected_count = 10
    actual_count = len(elements)
    assert expected_count == actual_count, f"expected {expected_count}, got {actual_count}"

