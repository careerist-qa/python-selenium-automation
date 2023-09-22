from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

LINKS = (By.CSS_SELECTOR, "class*='nav-tab-all_style_zg-tabs-li")

@given('Verify Bestsellers page is opened')
def verify_bestseller_page(context):
    actual_result = context.driver.find.element(LINKS)
    expected_result = len(LINKS) == 5
    assert actual_result == expected_result, f'Error expected {expected_result} does not match {actual_result}'