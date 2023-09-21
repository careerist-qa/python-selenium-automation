from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@then('Verify Bestsellers page is opened')
def verify_bestseller_page(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "class*='nav-tab-all_style_zg-tabs-li")
    expected_result = 5
    assert actual_result == expected_result, f'Error expected {expected_result} does not match {actual_result}'

